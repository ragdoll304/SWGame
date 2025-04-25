import streamlit as st
import uuid

# ✅ 전체 앱에 한 번 설정할 기본 배경
def bg():
    default_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXJqNTJibWh3bmtncHdyN2VwczN0azlzaWt0NGVyYnh6c2ozd3ByMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l3vRnoppYtfEbemBO/giphy.gif"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{default_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ 페이지별로 호출: 페이드인 애니메이션 포함된 배경
def bg2(gif_url: str):
    unique_class = f"bg-{uuid.uuid4().hex[:6]}"

    st.markdown(
        f"""
        <style>
        .{unique_class} {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-image: url("{gif_url}");
            background-size: cover;
            background-position: center;
            opacity: 0;
            animation: fadeIn 1.5s ease-in-out forwards;
            z-index: -1;
        }}
        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        </style>
        <div class="{unique_class}"></div>
        """,
        unsafe_allow_html=True
    )

def bg_cl():
     st.markdown(
            """
            <style>
            .stApp {
                background-image: none !important;
                background-color: transparent !important;
            }
            </style>
            """,
            unsafe_allow_html=True
    )