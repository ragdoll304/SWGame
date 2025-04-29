<<<<<<< HEAD
import streamlit as st
from view.ui.bg import bg # type: ignore

def a2():
    bg()  
    st.title("ㅁㄴㅇㅀㄴㅁㅇㄹ")

    if st.button("참가"):
        st.session_state.page = "scenario"
=======
import streamlit as st
from view.ui.bg import bg # type: ignore

def a2():
    bg()  
    st.title("ㅁㄴㅇㅀㄴㅁㅇㄹ")

    if st.button("참가"):
        st.session_state.page = "scenario"
>>>>>>> ec840f22c215b07b7ef1e8f610e7f3bbbe507b80
        st.rerun()