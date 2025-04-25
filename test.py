from view.ui.hide_bar import hide_bar_ui
from view.ui.bg import bg
from view.pages import start

import streamlit as st

#api

    ##여기서 작업하세용##

#logic

    ##여기서 작업하세용##

#guitar

    ##여기서 작업하세용##

#ui

hide_bar_ui() # 이거는 위에 창 숨기는 전체 영역 변수
bg() # 뒷 배경이므로 건들지 마세용

#page 시작
if "page" not in st.session_state:
    st.session_state.page = "start"

elif st.session_state.page == "lobby":
    lobby.start()



