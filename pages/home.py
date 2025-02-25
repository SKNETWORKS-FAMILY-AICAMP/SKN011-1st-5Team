import streamlit as st

def run():
    st.title("🏠신차 구매 트렌드 분석 및 FAQ 플랫폼")
    st.write("신차 구매 데이터를 활용해 연령별로 선호하는 차량을 시각화하여 제공하는 플랫폼입니다. 사이드바에서 원하는 기능을 선택해 주세요.")


    col1, col2 = st.columns([2, 1])  

    with col1:
        st.header("주요 기능")
        st.write("- 연령대별 많이 구매하는 차종 및 차량의 금액대")
        st.write("- FAQ 페이지: 신차 구매 관련 자주 묻는 질문 모음")


    with col2:
        st.header("📌 출처")
        st.write("출처 1 ")
        st.write("출처 2")

            