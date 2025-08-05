import streamlit as st
import os
from openai import OpenAI

st.title("Agent AI – Plan dnia")

prompt = st.text_area("Opisz swój dzień lub zostaw puste")

if st.button("Generuj plan"):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem planującym dzień."},
            {"role": "user", "content": prompt if prompt else "Zaplanuj mój dzień z czasem na pracę, sport i odpoczynek."}
        ]
    )

    st.write(response.choices[0].message.content)
