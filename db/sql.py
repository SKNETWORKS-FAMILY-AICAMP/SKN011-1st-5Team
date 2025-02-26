########## IMPORT
import mysql.connector
from car_class import *
##################################################



########## FUNCTION
# DB 생성
def create_car_db():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="ohgiraffers",
            password="ohgiraffers",
            database="menudb"
        )
        
        if connection.is_connected():
            print("MySQL에 성공적으로 연결되었습니다.")
            
            cursor = connection.cursor()
            
            sql = """
                CREATE DATABASE IF NOT EXISTS cardb;
                USE cardb;

                CREATE TABLE tbl_car (
                    car_id    INT PRIMARY KEY AUTO_INCREMENT,
                    
                    origin    TINYINT NOT NULL CHECK (origin IN (0, 1)),
                    company   VARCHAR(100) NOT NULL,
                    model     VARCHAR(100) NOT NULL,
                    fuel      VARCHAR(50) NOT NULL,
                    age       INT,
                    pur_count INT,
                    
                    --INDEX idx_analysis (origin, age, model)
                );
                """
            cursor.execute(sql)         
            print("cardb와 tbl_car를 생성하였습니다.")
            
            connection.commit()
            
        else:
            print("MySQL 연결에 실패했습니다.")
        
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        connection.close()
        


# Consumer list를 car_db에 데이터 삽입
def insert_car_db_to_Consumer(consumer_list):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="ohgiraffers",
            password="ohgiraffers",
            database="menudb"
        )
        
        if connection.is_connected():
            print("MySQL에 성공적으로 연결되었습니다.")
            
            cursor = connection.cursor()
            
            sql = """
                INSERT INTO CarsWithConsumers (origin, company, model, fuel, age, pur_count)
                VALUES (%s, %s, %s, %s, %s, %s)
                """

            # Consumer 리스트를 데이터로 변환
            data = [
                (consumer.origin, consumer.company, consumer.model, consumer.fuel, consumer.age, consumer.pur_count) for consumer in consumer_list
            ]
            
            # 여러 행 삽입
            cursor.executemany(sql, data)
            print(f"{cursor.rowcount}개의 행이 삽입되었습니다.")
                
            connection.commit()
            
        else:
            print("MySQL 연결에 실패했습니다.")
        
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        connection.close()
        
 
        
# car_db에서 데이터를 읽어 Consumer_list로 반환환
def get_Consumer_list():
    consumer_list = []
    
    connection = None
    cursor = None
        
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="ohgiraffers",
            password="ohgiraffers",
            database="menudb"
        )
        
        if connection.is_connected():
            print("MySQL에 성공적으로 연결되었습니다.")
            
            cursor = connection.cursor()
            
            sql = """
                SELECT origin, company, model, fuel, age, pur_count 
                FROM tbl_car
                """
            cursor.execute(sql)
            rows = cursor.fetchall()

            # Consumer 객체 리스트 생성
            
            for row in rows:
                origin_id, company_name, car_name, fuel, age, pur_count = row
                consumer = Consumer(origin_id, company_name, car_name, fuel, age, pur_count)
                consumer_list.append(consumer)

        else:
            print("MySQL 연결에 실패했습니다.")
        
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        connection.close()
    
    return consumer_list

##################################################