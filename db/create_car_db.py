import convert_to_list as convert
import sql as sql

# # db 생성
# sql.create_car_db()

# # 365데이터 바탕으로 데이터 삽입
# comsumer_list = convert.return_Consumer_list(convert.EXCEL_FILE_NAME)
# sql.insert_car_db_to_Consumer(comsumer_list)

consumers = sql.get_Consumer_list()
print(len(consumers))
for consumer in consumers:
    print(consumer)