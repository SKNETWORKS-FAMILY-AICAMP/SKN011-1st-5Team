import mysql.connector
import json


def convert_to_faq_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="ohgiraffers",
            password="ohgiraffers",
            database="faqdb"
        )

        cursor = connection.cursor()

        # hyundai - 0
        with open('../data/faq_hd.json', 'r', encoding='utf-8') as file:
            hd_data = json.load(file)

        for question, answer in hd_data.items():
            if question and answer:
                query = "insert into FAQ(QUESTION, ANSWER, COMPANY_ID) values (%s,%s,%s)"
                values = (question, answer,0)
                cursor.execute(query, values) 

        # kia
        with open('../data/faq_kia.json', 'r', encoding='utf-8') as file:
            kia_data = json.load(file)

        for d in kia_data:
            question = d['Q']
            answer = d['A']
            query = "insert into FAQ(QUESTION, ANSWER, COMPANY_ID) values (%s,%s,%s)"
            values = (question, answer,1)
            cursor.execute(query, values)

        connection.commit()
        print('데이터 삽입 완료')
        
    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
        connection.close()