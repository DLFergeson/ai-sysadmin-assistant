from nltk.tokenize import sent_tokenize
import nltk

nltk.download('punkt')

def extract_steps(text):
    sentences = sent_tokenize(text)
    action_keywords = ['configure', 'set', 'check', 'verify', 'install', 'restart', 'enable', 'disable', 'run']
    
    steps = []
    for sentence in sentences:
        if any(word in sentence.lower() for word in action_keywords):
            steps.append(sentence.strip())

    return steps
