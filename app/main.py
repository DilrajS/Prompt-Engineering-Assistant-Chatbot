import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load your OpenAI API key from an environment variable
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI API client
openai.api_key = OPENAI_API_KEY

def analyze_prompt(prompt):
    """
    Calls the OpenAI API to analyze the given prompt and return feedback.
    Replace "text-davinci-003" with your specific model, especially if you're using a fine-tuned version.
    """
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=100,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response.choices[0].text.strip()

def main():
    """
    The main function for the Streamlit application.
    It renders the UI components and handles the logic for prompt submission and displaying feedback.
    """
    st.title('Prompt Engineering Assistant Chatbot')

    user_prompt = st.text_area("Enter your prompt here to get feedback:", "")

    if st.button("Analyze Prompt"):
        if user_prompt:
            with st.spinner('Analyzing...'):
                feedback = analyze_prompt(user_prompt)
                st.write("Feedback:", feedback)
        else:
            st.warning("Please enter a prompt.")

if __name__ == '__main__':
    main()
