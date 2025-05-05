# AI SysAdmin Assistant

An intelligent AI-powered assistant designed for system administrators and network engineers.

## Features

- Validates SOPs from guides or work orders
- Extracts steps and verifies task completion
- Recommends automations (PowerShell/Python)
- Smart LLM-based question engine
- ConnectWise, Auvik, Automate, ITGlue integrations
- Web app (FastAPI), GUI (Tkinter), CLI
- Role-based access, HTML reports, Dockerized

## Quick Start

```bash
pip install -r requirements.txt
uvicorn web.main:app --reload
```

Or:

```bash
docker build -t ai-assistant .
docker run -p 8000:8000 ai-assistant
```
