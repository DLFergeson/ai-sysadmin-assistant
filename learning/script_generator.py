"""
Generates automation scripts in Python and PowerShell based on task descriptions.
"""

def generate_script_for_task(task_description):
    """
    Create basic task automation templates in Python and PowerShell.

    Args:
        task_description (str): Description of the system/network task.

    Returns:
        dict: Containing explanation, Python script, and PowerShell script.
    """
    explanation = f"Auto-generated scripts (Python and PowerShell) to perform: {task_description}"

    python_script = f"""#!/usr/bin/env python3

def main():
    print("Task: {task_description}")
    input_data = input("Enter any required input (e.g., IP address): ")
    print(f"Performing task with: {{input_data}}")

if __name__ == '__main__':
    main()
"""

    powershell_script = f"""# PowerShell Script for: {task_description}
param(
    [string]$InputData
)

Write-Host "Performing task: {task_description} with input: $InputData"
"""

    return {
        "explanation": explanation,
        "python_script": python_script,
        "powershell_script": powershell_script
    }
