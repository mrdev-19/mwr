import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from tempfile import NamedTemporaryFile
#---------------------------------------------------

page_title="MyWays.ai Results"
page_icon=""
layout="centered"

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)

hide_ele="""
        <style>
        #Mainmenu {visibility:hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        </style>
        """
st.markdown(hide_ele,unsafe_allow_html=True)

st.title(page_title+" "+page_icon)
st.header("Results ledu Bongu Ledu")
st.header("Fukk U !!")
st.header("Call me and Apologize now 😤😤😤")
st.image("fu.webp")
