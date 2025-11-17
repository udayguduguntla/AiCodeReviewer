import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_review_code(code):
    """
    Uses Groq LLM to analyze code and provide feedback.
    Model used: llama-3.1-8b-instruct
    """

    prompt = f"""
    You are an expert Python code reviewer and software architect.
    Review the following Python code and provide feedback in valid JSON format with these keys:
    
    {{
        "readability": "Describe code readability and structure.",
        "performance": "Mention any possible performance issues or improvements.",
        "security": "Point out potential security risks or unsafe code practices.",
        "code_quality": "Rate code quality as Excellent / Good / Fair / Poor.",
        "recommendations": "List 3 clear suggestions to improve the code."
    }}

    Python Code:
    {code}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        ai_output = response.choices[0].message.content.strip()

        # Try to extract valid JSON from response
        try:
            return json.loads(ai_output)
        except json.JSONDecodeError:
            import re
            match = re.search(r"\{.*\}", ai_output, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(0))
                except:
                    pass
            return {"error": "AI returned invalid JSON", "raw": ai_output}

    except Exception as e:
        return {"error": str(e)}
