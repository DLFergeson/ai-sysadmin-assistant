# 🛠️ Troubleshooting Guide

## Web App Not Starting
- Ensure `uvicorn` is installed
- Use `uvicorn web.main:app --reload`

## Script Not Executing
- Confirm script has `.py` or `.ps1` extension
- On Windows, allow PowerShell execution:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope Process
```

## Database Not Creating
- Delete `data/ai_assistant.db` and restart
- Check file permissions in `data/`

## API Keys Not Working
- Set keys in the `integrations/*.py` files
- Verify network/firewall access to APIs
