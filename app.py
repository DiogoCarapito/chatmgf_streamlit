import requests
import streamlit as st
#from streamlit_chat import message

# Define API endpoint
API_URL = 'https://diogocarapito-chatmgf.hf.space/run/predict'

# Define function to get API response
def get_api_response(input_text):
    response = requests.post(API_URL, json={"data": [input_text,]}).json()
    #return response["data"][0]
    return response["data"]


# Define Streamlit app
st.title('Chat:blue[MFG]')

conversation_history = []

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

user_input = st.text_input("Pergunta-me algo", "")
if st.button("Send"):
    api_response = get_api_response(user_input)
    st.session_state.conversation_history.append(("You", user_input))
    st.session_state.conversation_history.append(("ChatMGF", api_response[0]))
for speaker, text in st.session_state.conversation_history:
    st.text(f"{speaker}: {text}")

