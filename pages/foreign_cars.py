import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

st.set_page_config(layout="wide")

def run():
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("💡 수입 신차 판매 현황")

    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        data['orgin']
        total_data=[
            Consumer(orgin, company, model, ........),
            Consumer(orgin, company, model, ........),
            Consumer(orgin, company, model, ........),
            Consumer(orgin, company, model, ........),
            Consumer(orgin, company, model, ........),
            Consumer(orgin, company, model, ........),
            Consumer(orgin, company, model, ........),            
        ]

    df = pd.DataFrame(data)
    
    df = df[df['origin'] == 1]

    def categorize_age(age):
        if age < 30:
            return '20대'
        elif age < 40:
            return '30대'
        elif age < 50:
            return '40대'
        else:
            return '50대'

    df['age_group'] = df['age'].apply(categorize_age)

    age_categories = ["전체", "20대", "30대", "40대", "50대"]
    selected_category = st.radio("연령대를 선택하세요:", age_categories, horizontal=True)

    filtered_df = df.copy()
    if selected_category != "전체":
        filtered_df = filtered_df[filtered_df['age_group'] == selected_category]
    
    filtered_df = filtered_df.sort_values(by='pur_count', ascending=False)
    
    # 동적 데이터 로딩 (스크롤 시 추가 데이터 표시)
    rows_per_page = 10
    if "start_row" not in st.session_state:
        st.session_state.start_row = 0

    max_rows = len(filtered_df)
    visible_df = filtered_df.iloc[:st.session_state.start_row + rows_per_page]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("### 연령대별 상세 구매 데이터")
        st.dataframe(visible_df[['age_group', 'company', 'model', 'fuel', 'pur_count']], width=1200)
    
        if st.session_state.start_row + rows_per_page < max_rows:
            if st.button("더 보기"):
                st.session_state.start_row += rows_per_page
                st.rerun()
    
    with col2:
        st.write("### 연령대별 제조사 비율")
        fig, ax = plt.subplots(figsize=(6, 6))
        company_counts = filtered_df.groupby('company').sum(numeric_only=True)['pur_count']
        ax.pie(company_counts, labels=company_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

if __name__ == "__main__":
    run()