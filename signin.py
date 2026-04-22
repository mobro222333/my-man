import streamlit as st
st.markdown("<h1 style='text-align: center;'>sign up </h1>", unsafe_allow_html=True)
st.subheader("join us now")
with st.form("register_from"):
    st.subheader("personal information")
    col1, col2 = st.columns(2, border = True)
    col3, col4 = st.columns(2, border = True)
    col5, col6 = st.columns([2,1], border = True)

    with col1:
        full_name=st.text_input("full name")
    with col2:
        full_name=st.text_input("phone number")
    with col5:
        email=st.text_input("email")

    with col6:
        password=st.text_input("password",type="password")
    with col2:
        adress=st.text_input("adress")
    st.form_submit_button()

