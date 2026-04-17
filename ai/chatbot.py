import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_ai(user_query, context=""):
    prompt = f"""
    You are a smart assistant for a large sports stadium.

    Context:
    {context}

    User query:
    {user_query}

    Provide a short, clear, and helpful answer.
    """

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return response.candidates[0].content.parts[0].text

    except Exception as e:
        return "Unable to generate response at the moment."
