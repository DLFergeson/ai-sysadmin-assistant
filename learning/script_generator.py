from dotenv import load_dotenv; load_dotenv()

def generate_script_for_task(task_description):
    return {
        "explanation": f"Task: {task_description}",
        "python_script": "print('Python task')",
        "powershell_script": "Write-Host 'PS task'"
    }
