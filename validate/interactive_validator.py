"""
Interactive step-by-step validator using NLP and semantic analysis.
"""

from nlp.step_extractor import extract_steps
from nlp.answer_analyzer import is_answer_valid
from learning.activity_logger import log_activity

def validate_steps(content):
    """
    Run interactive validation on a guide's content.

    Args:
        content (str): Text extracted from a document or URL.

    Returns:
        list: Validation results per step with user responses and score.
    """
    print("\nExtracting procedural steps from guide...")
    steps = extract_steps(content)
    results = []

    if not steps:
        print("No actionable steps found in the guide.")
        return results

    print(f"\nFound {len(steps)} actionable steps.")
    for i, step in enumerate(steps):
        print(f"\nStep {i+1}: {step}")
        user_input = input("Did you complete this step? (Explain or describe): ")
        valid, score = is_answer_valid(step, user_input)
        results.append({
            "step": step,
            "response": user_input,
            "valid": valid,
            "score": score
        })

    log_activity("validation_results", results)
    return results
