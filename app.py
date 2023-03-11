import streamlit as st

st.set_page_config(
    page_title='ChatMFG',
    page_icon=':speech_balloon:'
)

st.session_state['answer'] = ''

st.markdown("# ChatMGF.com")
st.header("Welcome!")
with st.container():
    st.container()
    text_input = st.text_input('question', label_visibility='hidden', placeholder='Pergunta-me algo...')
    send = st.button('Enviar')
    if send:
        st.session_state['answer'] = st.session_state['answer'] + text_input

    st.write('##')

with st.container():
    st.write('---')
    st.header('About')
    st.write('tadadada')