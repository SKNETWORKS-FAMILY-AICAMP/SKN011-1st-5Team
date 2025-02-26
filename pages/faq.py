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

def search(word):
    pass

def show(data):
    df = pd.DataFrame(data, columns=["질문", "답변"])
    
    for index, row in df.iterrows():
        with st.expander(row["질문"]):  # 질문을 눌러야 답변이 보이게 설정
            st.write(row["답변"])  # 답변 표시


def run():
    create_connector()
    create_cursor()
    st.title("❓ 자주 묻는 질문 (FAQ)")

    selected_brand = st.radio("🚗 브랜드를 선택하세요:", ["현대", "기아"], horizontal=True)

    # word = st.text_input("🔍 검색할 단어를 입력하세요:")
    # if word:
    #     search(word)

    if selected_brand == "현대":
        query = "select question, answer from faq where company_id=0"
        data = load(query)
        show(data)
        
    elif selected_brand == "기아":
        query = "select question, answer from faq where company_id=1"
        data = load(query)
        show(data)

    

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