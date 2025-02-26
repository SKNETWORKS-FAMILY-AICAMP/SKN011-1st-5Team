import os
from crawler.faq_hyundai_crawler import crawl_hyundai
from crawler.faq_kia_crawler import crawl_kia
from db.faqdb_connector import convert_to_faq_db
import db.sql as sql
import db.convert_to_list as convert


# faq 관련 json파일 없으면 crawling 시작
exist_json = True
if not os.path.isfile("data/faq_hd.json"):
    crawl_hyundai()
    exist_json = False
if not os.path.isfile("data/faq_kia.json"):
    crawl_kia()
    exist_json = False
# db convert
if not (exist_json):
    convert_to_faq_db()
    
# cardb 확인
if (sql.check_car_db_tbl() == False):
    # db 생성
    sql.create_car_db()

    # 365데이터 바탕으로 데이터 삽입
    comsumer_list = convert.return_Consumer_list(convert.EXCEL_FILE_NAME)
    sql.insert_car_db_to_Consumer(comsumer_list)

    consumers = sql.get_Consumer_list()
    print(len(consumers))
    for consumer in consumers:
        print(consumer)
    

# streamlit 자동 실행
if __name__ == "__main__":
    os.system("streamlit run pages/main.py")  # app.py를 실행
    