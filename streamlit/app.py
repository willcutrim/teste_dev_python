import streamlit as st
from services.services import get_chatbot_response, get_all_chats

st.title("Chatbot")

user_message = st.text_input("Chat:", placeholder="Pergunte algo")

if st.button("Enviar", type="secondary", icon="💬"):
    try:
        if user_message:
            response = get_chatbot_response(user_message)
            st.write(f"Chatbot: {response}")
        else:
            st.write("Digite uma mensagem antes de enviar.")
            
    except Exception as e:
        st.write(f"Erro ao comunicar com o chatbot: {e}")

st.subheader("Histórico de Mensagens")
messages = get_all_chats()

st.write(f"Usuário: {messages}")
st.write(f"Chatbot: {messages}")
st.write(f"Data: {messages}")
st.write("---")  # Separador entre as mensagens