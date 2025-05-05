from learning.task_profiler import get_profile

def generate_recommendations(user_id):
    profile = get_profile(user_id)
    if not profile:
        return ["No profile data available yet. Complete more validations first."]

    recommendations = []

    if len(profile["missed_tasks"]) > len(profile["completed_tasks"]):
        recommendations.append("Consider reviewing fundamental procedures, as task success rate is low.")

    frequent_terms = profile.get("frequent_keywords", {})
    if 'verify' not in frequent_terms:
        recommendations.append("Add more verification steps to improve reliability.")

    if 'backup' not in frequent_terms:
        recommendations.append("Ensure backup procedures are consistently followed.")

    return recommendations
