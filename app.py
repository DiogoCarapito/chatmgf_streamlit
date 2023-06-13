import os
import requests
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import datetime


st.set_page_config(
    page_title='ChatMGF',
    page_icon=':broccoli:',
    layout='centered',
)

st.title(':broccoli: Chat:green[MGF]')
st.write('Pergunta-me algo')

# dotenv configuration
load_dotenv()  # Load variables from .env file

# gradio api
CHATMGF_API = os.getenv('CHATMGF_API')

# Supabase configuration
url: str = os.environ.get('SUPABASE_URL')
key: str = os.environ.get('SUPABASE_KEY')
supabase: Client = create_client(url, key)

# Define function to get API response
def get_api_response(input_text):
    # Get current datetime
    st.session_state['created_at'] = datetime.now().isoformat()
    # Get API response
    response = requests.post(CHATMGF_API,json={'data': [input_text,]}).json()
    # Create the data in a format to be inserted into Supabase
    sb_insert = {'created_at': st.session_state['created_at'], 'prompt': input_text, 'response': response['data'][0]}
    # Insert data into Supabase
    supabase.table('user_prompts_log').insert(sb_insert).execute()

    return response['data']



def register_feedback(prompt, response, feedback):
    data = supabase.table('user_prompts_log').select('id').eq('created_at', st.session_state['created_at']).execute()
    #st.success('Thanks!', icon='✅')
    return data
    #supabase.table('user_prompts_log').update({'feedback': feedback}).eq({'prompt', prompt, 'response', response}).execute()


if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''
if 'response' not in st.session_state:
    st.session_state['response'] = ''
if 'created_at' not in st.session_state:
    st.session_state['created_at'] = ''

# Add a text input and submit button so the user can enter a question
st.session_state['user_input'] = st.text_input('Pergunta-me algo', st.session_state['user_input'], label_visibility='hidden')

#st.write(':robot_face: **ChatMGF**:blue[ Olá, sou o ChatMGF. Pergunta-me algo]')

if st.session_state['user_input'] == '':
    pass
else:
    # Get API response
    api_response = get_api_response(st.session_state['user_input'])
    st.session_state['response'] = api_response[0]
    st.write(':smiley:', st.session_state['user_input'])
    st.write(f":broccoli: **Chat:green[MGF]**: {st.session_state['response']}")


#col_1, col_2, col_3 = st.columns([12,1,1])
#with col_1:
#    st.write(f":robot_face: **Chat:blue[MGF]**: {st.session_state['response']}")
#with col_2:
#    if st.button(':+1:', key='+1'):
#        st.write(register_feedback(st.session_state['user_input'],st.session_state['response'], 1))
#with col_3:
#    if st.button(':-1:', key='-1'):
#        st.write(register_feedback(st.session_state['user_input'],st.session_state['response'], -1))

