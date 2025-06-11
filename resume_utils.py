from resume_agent import ask_agent

def generate_bullets(role):
    prompt = f"Generate 3 impactful resume bullet points for: {role}"
    return ask_agent(prompt)

def review_resume(uploaded_file):
    content = uploaded_file.read().decode("utf-8")
    prompt = f"Review this resume and suggest improvements:\n\n{content}"
    return ask_agent(prompt)
