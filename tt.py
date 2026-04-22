import streamlit as st
home_page = st.Page(
page='home.py',
title = "home page",
icon='🦆',
default=True
)
chatbot_page = st.Page(
page='chatbot.py',
title = "chat with ai ",
icon='👌'
)

menue_page = st.Page(
page='menue.py', 
title = "menue page",
icon='👌'
)

signin_page = st.Page(
page='signin.py',
title = "sign in ",
icon="👍"
)
signup_page = st.Page(
page='signup.py',
title = "sign up ",
icon="👍"
)
all_pages=st.navigation(
pages=[home_page,
chatbot_page,
menue_page,
signin_page,
signup_page]
    , position="top"
)
all_pages.run()