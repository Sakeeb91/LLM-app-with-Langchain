import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

@st.cache(allow_output_mutation=True)
def get_llm(api_key):
    return OpenAI(temperature=0.7, openai_api_key=api_key)

def generate_response(llm, input_text):
    try:
        response = llm(input_text)
        st.info(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")

openai_api_key = st.sidebar.text_input('OpenAI API Key')

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')

    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')

    if submitted and openai_api_key.startswith('sk-'):
        llm = get_llm(openai_api_key)
        with st.spinner('Generating response...'):
            generate_response(llm, text)
