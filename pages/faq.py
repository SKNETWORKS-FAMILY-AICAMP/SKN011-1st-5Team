import streamlit as st
import json

def load_faq_data(brand):
    file_name = "faq_hyundai.json" if brand == "현대" else "faq_kia.json"
    
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error(f"🚨 {file_name} 파일을 찾을 수 없습니다.")
        return []

def run():
    st.title("❓ 자주 묻는 질문 (FAQ)")

    selected_brand = st.radio("브랜드를 선택하세요:", ["현대", "기아"], horizontal=True)

    faq_data = load_faq_data(selected_brand)

    search_query = st.text_input("🔍 검색할 단어를 입력하세요:")

    if search_query:
        filtered_faqs = [item for item in faq_data if search_query.lower() in item["Q"].lower()]
    else:
        filtered_faqs = faq_data  # 검색어 없을 경우 전체 표시

    
    if filtered_faqs:
        for item in filtered_faqs:
            with st.expander(item["Q"]):
                st.write(item["A"])
    else:
        st.warning("❌ 검색 결과가 없습니다.")