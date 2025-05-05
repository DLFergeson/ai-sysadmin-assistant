from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def is_answer_valid(expected_step, user_response, threshold=0.6):
    embeddings = model.encode([expected_step, user_response], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
    return similarity >= threshold, similarity
