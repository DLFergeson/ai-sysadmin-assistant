from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from validate.interactive_validator import validate_steps
from ingest.doc_ingestor import ingest_local_docs
from ingest.web_ingestor import ingest_web_article
from learning.task_profiler import update_profile
from learning.recommendation_engine import generate_recommendations
from reports.report_generator import generate_html_report
from learning.script_generator import generate_script_for_task
import uuid

app = FastAPI()
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": ""})

@app.post("/validate", response_class=HTMLResponse)
async def handle_validate(request: Request, user_id: str = Form(...), content: str = Form(...)):
    results = validate_steps(content)
    update_profile(user_id, results)
    recommendations = generate_recommendations(user_id)
    report_html = generate_html_report(user_id, results, recommendations)

    report_path = f"data/{user_id}_report.html"
    with open(report_path, "w") as f:
        f.write(report_html)

    return templates.TemplateResponse("report.html", {
        "request": request,
        "user_id": user_id,
        "results": results,
        "recommendations": recommendations,
        "report_url": f"/static/reports/{user_id}_report.html"
    })

@app.post("/generate-script", response_class=HTMLResponse)
async def generate_script(request: Request, task_description: str = Form(...)):
    script, explanation = generate_script_for_task(task_description)
    script_id = str(uuid.uuid4())
    path = f"scripts/generated_{script_id}.py"
    with open(path, "w") as f:
        f.write(script)

    return templates.TemplateResponse("script.html", {
        "request": request,
        "script": script,
        "explanation": explanation,
        "filename": f"generated_{script_id}.py"
    })

from learning.script_executor import execute_script
from data.db_models import SessionLocal, User

@app.post("/run-script", response_class=HTMLResponse)
async def run_script(request: Request, username: str = Form(...), script_path: str = Form(...)):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user or not user.is_admin():
        return HTMLResponse("<h3>Access denied: Only admins can execute scripts.</h3>", status_code=403)

    output, success = execute_script(script_path)
    return templates.TemplateResponse("output.html", {
        "request": request,
        "username": username,
        "script_path": script_path,
        "output": output,
        "status": "Success" if success else "Failed"
    })

from integrations.itglue import search_docs as search_itglue
from integrations.auvik import get_device_status

@app.post("/search-docs", response_class=HTMLResponse)
async def search_docs(request: Request, search_term: str = Form(...)):
    itglue_matches = search_itglue(search_term)
    auvik_status = get_device_status(search_term)

    return templates.TemplateResponse("search_results.html", {
        "request": request,
        "term": search_term,
        "docs": itglue_matches,
        "device": auvik_status
    })
