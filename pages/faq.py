import streamlit as st
import mysql.connector
import pandas as pd

def create_connector():
    connection = mysql.connector.connect(
        host="localhost",
        user="ohgiraffers",
        password="ohgiraffers",
        database="faqdb"
    )
    return connection

def create_cursor():
    connection = create_connector()
    cursor = connection.cursor()
    return connection, cursor

def load(query):
    connection, cursor = create_cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    connection.close()
    return data

def show(data, word=None):
    df = pd.DataFrame(data, columns=["질문", "답변"])

    if word:
        df = df[df["질문"].str.contains(word, case=False, na=False) | 
            df["답변"].str.contains(word, case=False, na=False)]
    
    for _, row in df.iterrows():
        with st.expander(row["질문"]):
            st.write(row["답변"]) 


def run():
    create_connector()
    create_cursor()
    st.title("❓ 자주 묻는 질문 (FAQ)")

    selected_brand = st.radio("🚗 브랜드를 선택하세요:", ["현대", "기아"], horizontal=True)

    word = st.text_input("🔍 검색할 단어를 입력하세요:")

    if selected_brand == "현대":
        query = "select question, answer from faq where company_id=0"
        data = load(query)
        show(data, word)
        
    elif selected_brand == "기아":
        query = "select question, answer from faq where company_id=1"
        data = load(query)
        show(data, word)

    

    # if search_query:
    #     filtered_faqs = [item for item in faq_data if search_query.lower() in item["Q"].lower()]
    # else:
    #     filtered_faqs = faq_data  # 검색어 없을 경우 전체 표시

    
    # if filtered_faqs:
    #     for item in filtered_faqs:
    #         with st.expander(item["Q"]):
    #             st.write(item["A"])
    # else:
    #     st.warning("❌ 검색 결과가 없습니다.")