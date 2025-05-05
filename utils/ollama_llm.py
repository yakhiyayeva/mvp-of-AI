import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

def ask_ollama(question, context):
    prompt = f"""
You are a helpful AI assistant for the Constitution of the Republic of Kazakhstan.
Use the following context to answer the question. Be concise and accurate.

Context:
{context}

Question:
{question}

Answer:
"""
    result = subprocess.run(
        ["ollama", "run", OLLAMA_MODEL],
        input=prompt.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8").strip()
