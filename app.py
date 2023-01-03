import streamlit as st
import requests
#from streamlit_lottie import st_lottie

st.set_page_config(page_title="Lycamobile",page_icon=":green_heart:",layout="wide")

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")



#HEADER
st.title("Lycamobile:green_heart:")
st.subheader("We deliver sim cards at your home for free")

st.write("---")
st.subheader("How to get")
st.write(
    """
    - Just drop your address in the contact form below
    - You will recieve them at your address within 24 hours
    """)
st.write("---")
st.subheader("Contact Us")
contact_form="""
<form action="https://formsubmit.co/jensonantony500@gmail.com" method="POST">
     <input type="email" name="email" placeholder="Your email" required>
     <input type="text" name="address" placeholder="Your Address" required>
     <input type="text" name="message" placeholder="Message(optional)">
     <button type="submit">Send</button>
</form>
"""
#left_column,right_column=st.columns(2)
#with left_column:
st.markdown(contact_form,unsafe_allow_html=True)