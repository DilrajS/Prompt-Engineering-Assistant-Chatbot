import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI API client
openai.api_key = OPENAI_API_KEY

def optimize_prompt(prompt_text):
    """
    Calls the fine-tuned OpenAI model to analyze and return an optimized version of the given prompt. 
    """
    response = openai.Completion.create(
        model="your_fine_tuned_model_id",  # Replace with your fine-tuned model's ID
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    optimized_prompt = response.choices[0].text.strip()
    return optimized_prompt
