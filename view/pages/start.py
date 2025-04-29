<<<<<<< HEAD
import streamlit as st
from view.ui.bg import bg  # type: ignore

def a1():
    bg()
    st.title("AMI")
    st.write("시작 페이지입니다.")
    
    if st.button("게임 시작"):
        st.session_state.page = "lobby"
=======
import streamlit as st
from view.ui.bg import bg  # type: ignore

def a1():
    bg()
    st.title("AMI")
    st.write("시작 페이지입니다.")
    
    if st.button("게임 시작"):
        st.session_state.page = "lobby"
>>>>>>> ec840f22c215b07b7ef1e8f610e7f3bbbe507b80
        st.rerun()