<<<<<<< HEAD
import streamlit as st
from view.ui.bg import bg2, bg_cl  # type: ignore

def a3():
    bg_cl()
    bg2("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmpqMmZjbXhhNjNqY2NnZjh0OTI2bGVtNzFldGh6c3Fkamh0emVkMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PNQi3nT7CVE3JFiRot/giphy.gif")
    st.title("시나리오 써봐라")

    if st.button("제출"):
        st.session_state.page = "prompf"
=======
import streamlit as st
from view.ui.bg import bg2, bg_cl  # type: ignore

def a3():
    bg_cl()
    bg2("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmpqMmZjbXhhNjNqY2NnZjh0OTI2bGVtNzFldGh6c3Fkamh0emVkMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PNQi3nT7CVE3JFiRot/giphy.gif")
    st.title("시나리오 써봐라")

    if st.button("제출"):
        st.session_state.page = "prompf"
>>>>>>> ec840f22c215b07b7ef1e8f610e7f3bbbe507b80
        st.rerun()