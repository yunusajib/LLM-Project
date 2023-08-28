import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
os.environ['OPENAI_API_KEY']= apikey

#App framework
st.title('Youtube GPT Creator')
prompt = st.text_input(" plug in Prompt here")

#prompt template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'write me a youtube video topic about{topic}'
)
script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template = 'write me a youtube video script about this title TITLE:{title} while leveraging this wikipedia research:{wikipedia_research}'

)
#MEmory
title_memory = ConversationBufferMemory(input_key= 'topic', memory_key = 'chat_history')
script_memory = ConversationBufferMemory(input_key= 'title', memory_key = 'chat_history')


#llm model
llm = OpenAI(temperature =0.9)
title_chain = LLMChain(llm=llm, prompt = title_template,  verbose= True, output_key = 'title', memory = title_memory)
script_chain = LLMChain(llm=llm, prompt = script_template, verbose= True, output_key = 'script', memory = script_memory)

wiki = WikipediaAPIWrapper()

#show stuff to the screen if there is a prompt
if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title= title, wikipedia_research= wiki_research)
    st.write(title)
    st.write(script)

    with st.expander('title_history'):
        st.info(title_memory.buffer)
    with st.expander('script_history'):
        st.info(script_memory.buffer)
    with st.expander('wikipedia_research_history'):
        st.info(wiki_research)