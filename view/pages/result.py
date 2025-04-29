<<<<<<< HEAD
import streamlit as st
from view.ui.bg import bg2,bg_cl  # type: ignore

def a5():
    bg_cl()
    bg2("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmE3bTEyMW01bnltaGVyeTR4OXNlcDkxYWpndjhsamN0Nzg2Njk5cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kg19fN5BXbZGIDznzG/giphy.gif")
    st.title("결과")

    if st.button("ㅎㅁㄴㅇ"):
        st.session_state.page = "reseult"
=======
import streamlit as st
from view.ui.bg import bg2,bg_cl  # type: ignore

def a5():
    bg_cl()
    bg2("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmE3bTEyMW01bnltaGVyeTR4OXNlcDkxYWpndjhsamN0Nzg2Njk5cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kg19fN5BXbZGIDznzG/giphy.gif")
    st.title("결과")

    if st.button("ㅎㅁㄴㅇ"):
        st.session_state.page = "reseult"
>>>>>>> ec840f22c215b07b7ef1e8f610e7f3bbbe507b80
        st.rerun()