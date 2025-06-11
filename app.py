import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit UI
st.title("AI Blog Writer ✍️")
st.subheader("Shiv says let AI do its magic!")

with st.sidebar:
    st.title("Blog Controls")
    blog_title = st.text_input("Blog Title")
    keywords = st.text_input("Keywords (comma-separated)")
    word_count = st.slider("Word Count", 100, 1000, 300, 100)
    submit_button = st.button("Generate Blog")

# When the user clicks the button
if submit_button:
    if not blog_title or not keywords:
        st.warning("Please provide a title and keywords.")
    else:
        with st.spinner("Generating blog..."):
            prompt = f"""Write a blog titled "{blog_title}" using the keywords: {keywords}.
            The blog should be approximately {word_count} words.
            Make it engaging and informative."""

            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            st.subheader("Generated Blog")
            st.write(response.text)

st.markdown("""Created by Shiv Bhardwaj""")