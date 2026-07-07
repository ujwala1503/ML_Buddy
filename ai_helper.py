from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def ask_ml_buddy(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are ML Buddy, a friendly Machine Learning tutor for beginners. Explain concepts in simple English with examples."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content