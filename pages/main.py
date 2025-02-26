import streamlit as st

import home
import korean_cars
import foreign_cars
import faq

st.sidebar.title("메뉴")

page = st.sidebar.radio(
    "이동할 페이지를 선택하세요:",
    ["Home", "💡 국산 신차 판매 현황", "✨ 수입 신차 판매 현황", "❓ FAQ"]
)


def run_selected_page(page_name):
    if page_name == "🏠 Home":
        home.run()
    elif page_name == "💡 국산 신차 판매 현황":
        korean_cars.run()
    elif page_name == "✨ 수입 신차 판매 현황":
        foreign_cars.run()
    elif page_name == "❓ FAQ":
        faq.run()

run_selected_page(page)