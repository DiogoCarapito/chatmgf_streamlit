import requests
import streamlit as st

# Define API endpoint
API_URL = 'https://diogocarapito-chatmgf.hf.space/run/predict'

def get_api_response(input_text):
    data = {"input_text": input_text}
    response = requests.post(API_URL, data).json()
    return response["data"]


# Define function to get API response
def get_api_response(input_text):
    response = requests.post(API_URL, json={
        "data": [
            input_text,
        ]
    }).json()
    return response["data"][0]


# Define Streamlit app
def main():
    st.title('Chat:blue[MFG]')
    conversation_history = []
    user_input = st.text_input("Pergunta-me algo", "")
    if st.button("Send"):
        api_response = get_api_response(user_input)
        conversation_history.append(("You", user_input))
        conversation_history.append(("Chatbot", api_response))
    for speaker, text in conversation_history:
        st.text(f"{speaker}: {text}")

if __name__ == "__main__":
    main()