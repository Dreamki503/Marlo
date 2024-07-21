import streamlit as st
from streamlit_option_menu import option_menu
import dashboard

st.set_page_config(page_title="Marlo")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title" : title,
            "function" : function
        })

    def run():
        with st.sidebar :
            #app = "Chat"
            app = option_menu(
                menu_title= "Menu",
                options = ["Dashboard"],
                icons = ["chat-text-fill","person-circle","camera"],
                default_index= 0,
                styles = {
                    "icons" :{"color" : "white"}
                }
            )
        if app == "Dashboard":
            dashboard.app()

    run()