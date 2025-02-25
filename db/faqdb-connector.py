import mysql.connector
import json

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="faqdb"
)

cursor = connection.cursor()

with open('../data/faq_hd.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for question, answer in data.items():
    if question and answer:
        insert_query = "insert into FAQ(QUESTION, ANSWER) values (%s,%s)"
        cursor.execute(insert_query, (question, answer)) 

connection.commit()

cursor.close()
connection.close()

print('데이터 삽입 완료')

