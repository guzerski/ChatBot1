import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
modeloIA = OpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

st.write("## ChatBot de IA teste")
mensagem_usuario = st.chat_input("Digite sua mensagem aqui...")

if mensagem_usuario:
    mensagem1 = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem1) 

    resposta_modelo = modeloIA.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )
    resposta_ia = resposta_modelo.choices[0].message.content

    mensagem2 = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem2)
  
for mensagem in st.session_state["lista_mensagens"]:
    if mensagem["role"] == "user":
        st.chat_message("user").write(mensagem["content"])
    else:
        st.chat_message("assistant").write(mensagem["content"])