from ingest.doc_ingestor import ingest_local_docs
from ingest.web_ingestor import ingest_web_article
from learning.activity_logger import log_activity

def run_cli():
    print("Welcome to the AI Assistant (CLI Mode)")
    source = input("Enter input type (file/url): ").strip().lower()

    if source == 'file':
        path = input("Enter file path: ")
        content = ingest_local_docs(path)
    elif source == 'url':
        url = input("Enter article URL: ")
        content = ingest_web_article(url)
    else:
        print("Invalid input type.")
        return

    log_activity("ingested_guide", {"source": source, "content_sample": content[:100]})
    print("\nGuide ingested. (Preview below)\n")
    print(content[:500])

from validate.interactive_validator import validate_steps

    results = validate_steps(content)
    success_rate = sum(1 for r in results if r['valid']) / len(results) * 100 if results else 0
    print(f"\nValidation complete. Success rate: {success_rate:.2f}%")
