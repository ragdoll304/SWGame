import streamlit as st
from view.ui.bg import bg # type: ignore

def a2():
    bg()  
    st.title("ㅁㄴㅇㅀㄴㅁㅇㄹ")

    if st.button("참가"):
        st.session_state.page = "scenario"
        st.rerun()