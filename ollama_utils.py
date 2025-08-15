import requests

def get_reflection(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:latest",
                "prompt": f"You are a calm, kind mental health companion. A user says: '{prompt}'. Give a helpful and warm reflection."
            }
        )
        output = response.json()
        print("🧠 Ollama raw response:", output)  # Add this for debugging
        return output.get("response", "Sorry, I couldn't understand.")
    except Exception as e:
        print("❌ Ollama error:", e)
        return "Error: Could not connect to the AI. Is Ollama running?"
