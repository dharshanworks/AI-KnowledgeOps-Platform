from groq import Groq

from utils.config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


SYSTEM_PROMPT = """
You are an AI assistant for an Enterprise Knowledge Base.

Answer ONLY using the provided context.

If the answer is not present in the context, reply exactly:

I could not find the answer in the uploaded document.
"""


def generate_answer(question: str, context: str) -> str:
    """
    Generate an answer using the Groq LLM.
    """

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.2,
        max_completion_tokens=512,
    )

    return response.choices[0].message.content