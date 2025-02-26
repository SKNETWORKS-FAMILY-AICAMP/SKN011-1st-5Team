import sys
import os

# 현재 파일(foreign_cars.py) 기준 상위 디렉토리를 sys.path에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st  
import pandas as pd
import matplotlib.pyplot as plt
import db.sql as sql 
import matplotlib.font_manager as fm

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def run():
    st.title("💡 국산 신차 판매 현황")

    try:
        consumers = sql.get_Consumer_list()

        # 데이터가 없거나 오류 발생 시 방어 코드
        if consumers is None or len(consumers) == 0:
            st.error("❌ 데이터베이스에서 데이터를 불러오지 못했습니다.")
            return
    except Exception as e:
        st.error(f"❌ 데이터를 불러오는 중 오류 발생: {e}")
        return

    data = [(c.origin, c.company, c.model, c.fuel, c.age, c.pur_count) for c in consumers]
    df = pd.DataFrame(data, columns=['origin', 'company', 'model', 'fuel', 'age', 'pur_count'])
    
    df = df[df['origin'] == 0]

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
    
    st.write("### 연령대별 상세 구매 데이터")
    st.dataframe(visible_df[['age_group', 'company', 'model', 'fuel', 'pur_count']], width=1400)

    if st.session_state.start_row + rows_per_page < max_rows:
        if st.button("더 보기"):
            st.session_state.start_row += rows_per_page
            st.rerun()
    
    # 연령대별 제조사 비율 파이 차트
    st.write("### 연령대별 제조사 비율")
    
    fig, ax = plt.subplots(figsize=(16, 10))
    company_counts = filtered_df.groupby('company').sum(numeric_only=True)['pur_count']
    company_counts = company_counts.sort_values(ascending=False).head(10)  # 상위 10개만 선택
    

    colors = plt.cm.Paired.colors[:len(company_counts)]

    wedges, _, autotexts = ax.pie(
        company_counts,
        labels=None,  
        autopct='%1.1f%%',  
        startangle=90,
        colors=colors,
        textprops={'fontsize': 20, 'color': 'white'} 
    )

    ax.axis('equal')

    legend_labels = [f"{company} ({percent:.1f}%)" for company, percent in zip(company_counts.index, (company_counts / company_counts.sum()) * 100)]
    ax.legend(wedges, legend_labels, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=20)
    
    st.pyplot(fig)

if __name__ == "__main__":
    run()