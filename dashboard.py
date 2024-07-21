import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def app():
    st.title("Welcome to :green[Marlo]")
    st.subheader("How can I help you today!")
    st.divider()
    client = Groq(api_key=os.getenv("API_KEY"))

    def draft_message(content, role = "user"):
        return {
            "content" : content,
            "role" : role
        }
    
    if "messages" not in st.session_state :
        st.session_state.messages = []
    
    if "system_message_added" not in st.session_state:
            st.session_state.messages.append(
                {
                    "role" : "system",
                    "content" : "you are a helpful Certified Management Accounting professor."
                }
            )
            st.session_state.system_message_added = True

    for message in st.session_state.messages:
         if message["role"] != "system" :
              with st.chat_message(message["role"]):
                   st.markdown(message["content"])

    prompt = st.chat_input("Enter something")
    
    if prompt:
        with st.chat_message("user"):
             st.markdown(prompt)
        
        st.session_state.messages.append(draft_message(prompt))

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # Collect messages for the conversation
            conversation = st.session_state.messages.copy()
            conversation.append(draft_message(prompt))

            response = client.chat.completions.create(temperature = 1,
                model= "llama3-70b-8192",
                max_tokens= 1000,
                messages= conversation)
            
            response.usage.total_tokens

            content = response.choices[0].message.content
            full_response += content
            message_placeholder.markdown(full_response + "|")

            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
