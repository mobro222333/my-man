
import streamlit as st
st.markdown("<h1 style='text-align: center;'>Welcome to Pizza Hub</h1>", unsafe_allow_html=True)
st.subheader("serving pizza an pasta ")
st.image("hero.JPG")
st.divider()
col1, col2 = st.columns(2, border = True)

with col1:
    st.subheader("need help")
    st.write("chat with ai")
    if st.button("ai"):
            st.switch_page("chatbot.py")
with col2:
    st.subheader("hungry")
    st.write("show the menue")

    if st.button("menue"):
            st.switch_page("menue.py")