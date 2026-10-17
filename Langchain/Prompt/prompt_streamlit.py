from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
st.title("Movie Summary generator")
user_input=st.text_input("Enter the name of the movie")
if st.button("Generate Summary"):
    response = model.invoke(user_input)
    st.write(response.content)