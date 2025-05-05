import datetime

def generate_html_report(user_id, results, recommendations):
    html = f"""<html>
    <head><title>Validation Report</title><style>
    body {{ background: #121212; color: #e0e0e0; font-family: sans-serif; padding: 20px; }}
    h1 {{ color: #90caf9; }}
    .step {{ margin-bottom: 1em; }}
    .valid {{ color: #81c784; }}
    .invalid {{ color: #e57373; }}
    </style></head><body>
    <h1>Validation Report for {user_id}</h1>
    <p><b>Date:</b> {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <hr>
    <h2>Step Results</h2>
    """

    for r in results:
        status = "valid" if r["valid"] else "invalid"
        html += f"""<div class='step'><b>Step:</b> {r['step']}<br>
                  <b>Your Response:</b> {r['response']}<br>
                  <b>Status:</b> <span class='{status}'>{status.upper()}</span><br>
                  <b>Score:</b> {r['score']:.2f}</div>"""

    html += "<hr><h2>Recommendations</h2><ul>"
    for rec in recommendations:
        html += f"<li>{rec}</li>"
    html += "</ul></body></html>"

    return html
