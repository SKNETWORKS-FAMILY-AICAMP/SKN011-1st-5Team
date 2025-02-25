import streamlit as st

def run():
    st.title("💡수입 신차 판매 현황")

    age_categories = ["전체", "20대", "30대", "40대", "50대"]
    selected_category = st.radio("연령대를 선택하세요:",age_categories, horizontal=True)