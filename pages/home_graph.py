import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

def create_connector():
    connection = mysql.connector.connect(
        host="localhost",
        user="ohgiraffers",
        password="ohgiraffers",
        database="cardb"
    )
    return connection

def load_data():
    query = """
        SELECT 
            age, 
            SUM(pur_count) AS total_purchases
        FROM tbl_car
        WHERE age IS NOT NULL
        GROUP BY age
        ORDER BY age;
    """
    connection = create_connector()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    
    df = pd.DataFrame(result, columns=["Age", "Total Purchases"])
    return df

def run():
    st.header("📊 Age별 총 구매 수")

    df = load_data()

    fig, ax = plt.subplots()
    ax.bar(df["Age"], df["Total Purchases"], color="#FFABAB", width=7)
    ax.set_xlabel("Age")
    ax.set_ylabel("Toal Purchase")
    # ax.set_title("Age별 총 구매 수")

    # x축의 눈금 간격을 10으로 설정
    ax.set_xticks(range(20, int(df["Age"].max()) + 10, 10))

    st.pyplot(fig)
