import streamlit as st

def hide_bar_ui():
    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .viewerBadge_container__1QSob,
        .viewerBadge_link__1S137,
        .viewerBadge_container__1QSob {
            display: none !important;
        }

        .block-container {
            padding-top: 0rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

                