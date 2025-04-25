from view.ui.hide_bar import hide_bar_ui

from view.ui.bg import bg

from view.pages import start,lobby,scenario,prompf,result


import streamlit as st
#api

    ##여기서 작업하세용##

#logic

    ##여기서 작업하세용##

#guitar

    ##여기서 작업하세용##

#ui
hide_bar_ui() # 이거는 위에 창 숨기는 전체 영역 함수

#page 시작
if "page" not in st.session_state:
    st.session_state.page = "start"

if st.session_state.page == "start":
    start.a1()
elif st.session_state.page == "lobby":
    lobby.a2()
elif st.session_state.page == "scenario":
    scenario.a3()
elif st.session_state.page == "prompf":
    prompf.a4()
elif st.session_state.page == "result":
    result.a5()


