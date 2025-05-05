"""
Simple GUI mode using Tkinter. Default dark theme.
"""

import tkinter as tk
from tkinter import filedialog, simpledialog, scrolledtext
from ingest.doc_ingestor import ingest_local_docs
from ingest.web_ingestor import ingest_web_article
from validate.interactive_validator import validate_steps
from learning.task_profiler import update_profile
from learning.recommendation_engine import generate_recommendations
from reports.report_generator import generate_html_report

def run_gui():
    """Launch the Tkinter-based graphical interface."""
    app = tk.Tk()
    app.title("AI Assistant")
    app.configure(bg="#121212")
    app.geometry("800x600")

    def run_validation():
        """Trigger validation process from file or URL input."""
        user_id = simpledialog.askstring("User", "Enter your user ID:")
        src_type = simpledialog.askstring("Source Type", "file or url?")
        content = ""

        if src_type == "file":
            path = filedialog.askopenfilename()
            content = ingest_local_docs(path)
        elif src_type == "url":
            url = simpledialog.askstring("URL", "Enter article URL:")
            content = ingest_web_article(url)

        if content:
            results = validate_steps(content)
            update_profile(user_id, results)
            recommendations = generate_recommendations(user_id)
            html = generate_html_report(user_id, results, recommendations)

            with open(f"data/{user_id}_report.html", "w") as f:
                f.write(html)

            output.delete('1.0', tk.END)
            output.insert(tk.END, f"Report generated: data/{user_id}_report.html\n")
            for r in recommendations:
                output.insert(tk.END, f"- {r}\n")

    tk.Button(app, text="Run Validation", command=run_validation, bg="#1e88e5", fg="white").pack(pady=20)
    output = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=100, height=25, bg="#212121", fg="#ffffff")
    output.pack(padx=10, pady=10)

    app.mainloop()
