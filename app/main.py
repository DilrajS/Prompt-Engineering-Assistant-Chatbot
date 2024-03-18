import streamlit as st
from app.utils import analyze_prompt  # Assuming utils.py is in an 'app' package

def main():
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
