import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI API client
openai.api_key = OPENAI_API_KEY

def analyze_prompt(prompt_text):
    """
    Calls the OpenAI API to analyze the given prompt and return feedback.
    Adjust as necessary for your application.
    """
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt_text,
      temperature=0.7,
      max_tokens=100,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response.choices[0].text.strip()
