import mysql.connector
import json

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="faqdb"
)

cursor = connection.cursor()

# hyundai
with open('../data/faq_hd.json', 'r', encoding='utf-8') as file:
    hd_data = json.load(file)

for question, answer in hd_data.items():
    if question and answer:
        insert_query = "insert into FAQ(QUESTION, ANSWER) values (%s,%s)"
        cursor.execute(insert_query, (question, answer)) 

# kia
with open('../data/faq_kia.json', 'r', encoding='utf-8') as file:
    kia_data = json.load(file)

for d in kia_data:
    question = d['Q']
    answer = d['A']
    insert_query = "insert into FAQ(QUESTION, ANSWER) values (%s,%s)"
    cursor.execute(insert_query, (question, answer)) 

connection.commit()

cursor.close()
connection.close()

print('데이터 삽입 완료')

