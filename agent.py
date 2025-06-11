import subprocess

def ask_agent(prompt):
    cmd = ["ollama", "run", "phi3", prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()
