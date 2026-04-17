import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro")

def ask_ai(user_query, context=""):
    prompt = f"""
    You are a smart assistant for a large sports stadium.

    Context:
    {context}

    User query:
    {user_query}

    Provide a short, clear, and helpful answer.
    """

    response = model.generate_content(prompt)
    return response.text
