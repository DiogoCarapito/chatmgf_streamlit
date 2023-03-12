import streamlit as st
#import openai
import os

openai_api_key = os.environ.get('OPENAI_API_KEY')

st.set_page_config(
    page_title='ChatMGF',
    page_icon=':blue_book:'
)
#st.session_state.answer = []

st.title('Chat:blue[MFG]')

with st.container():
    st.session_state.answer = st.session_state.answer + [st.text_input('question', label_visibility='hidden', placeholder='Pergunta-me algo...')]
    st.write(st.session_state.answer)
