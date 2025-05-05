# 📦 Installation Guide

## Prerequisites
- Python 3.10+
- Git (optional, for cloning)
- pip
- (Optional) Docker

## 1. Clone or Download
```bash
git clone https://your-repo-url.git
cd ai_sysadmin_assistant
```

## 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 3. Run Locally
```bash
uvicorn web.main:app --reload
```

## 4. Build & Run Docker (Optional)
```bash
docker build -t ai-assistant .
docker run -p 8000:8000 ai-assistant
```
