import streamlit as st
import home_graph as hg

def run():
    st.title("🏠신차 구매 트렌드 분석 및 FAQ")
    st.write("신차 구매 데이터를 활용해 연령별로 선호하는 차량을 시각화하여 제공하는 플랫폼입니다. 사이드바에서 원하는 기능을 선택해 주세요.")


    col1, col2 = st.columns([3, 2])  

    with col1:
        st.header("✅ 주요 기능")
        st.write("- 연령대별 자동차 등록 현황 \n - 연령대별 국내 신차 판매 현황 \n - 연령대별 수입 신차 판매 현황")


    with col2:
        st.header("📌 출처")
        st.markdown("[자동차 신차구입 조회 사이트](https://www.car365.go.kr/web/contents/newcar_analysis.do)")
        st.markdown("[현대 차량 구매 FAQ](https://www.hyundai.com/kr/ko/e/customer/center/faq)")
        st.markdown("[기아 차량 구매 FAQ](https://www.kia.com/kr/customer-service/center/faq)")

    hg.run()    