import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# to load all your environment variables from .env file
load_dotenv()

# to configure the page
st.set_page_config(page_title="Simple Chatbot")

# The title
st.title("Suhavani's Simple Gemini Chatbot")
st.write("Ask me anything!")

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    # Configuring gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-flash-latest')
    
    # User input
    user_question = st.text_input("Your question:", key="question")
    
    # Send the input when button is clicked or enter is pressed
    if (st.button("Send") or user_question) and user_question:
        with st.spinner("Thinking..."):
            try:
                # Basic response
                response = model.generate_content(user_question) #Comment this for advanced chatbot
                
                # Advanced Chatbot: Make AI act like different characters (comment out the line above and uncomment below 3 lines)
                #system_prompt = "You are a friendly pirate captain. Always talk like a pirate with 'Ahoy!' and 'Arrr!'"
                #full_prompt = f"{system_prompt}\n\nUser: {user_question}\nPirate:"
                #response = model.generate_content(full_prompt)

                # MORE CHARACTER IDEAS (just replace the system_prompt):
                # system_prompt = "You are a wise wizard who speaks in riddles"
                # system_prompt = "You are a helpful cooking chef who gives cooking tips"
                # system_prompt = "You are a motivational fitness trainer"
                # system_prompt = "You are Shakespeare writing in old English"
                
                # Displaying the response
                st.write("**Bot:**", response.text)
                
            except Exception as e:
                st.error("Something went wrong! Please check your API key in .env file.")
else:
    st.error("API key not found! Please add your GEMINI_API_KEY to the .env file.")