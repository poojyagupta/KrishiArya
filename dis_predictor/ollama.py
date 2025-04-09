from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
#Converts the template into a structured message ready to be used by an LLM.

from langchain_core.output_parsers import StrOutputParser
#cleans up the output to be understood by the user
#output may contain extra metadata or formatting, this thing removes all that

from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.")
        ("user", "Question:{question}")
        
    ]
)

st.title("Welcome to KrishiArya")
input_text = st.text_input("What can i help you with?")

#openai llm, which llm to use

llm = ChatOpenAI(model = "gpt-4")

#now the parser or the output fixer
output_parser = StrOutputParser

#total direction to my output(the workflow)
chain = prompt|llm|output_parser