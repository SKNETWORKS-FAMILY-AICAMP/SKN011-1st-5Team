########## IMPORT
from enum import Enum
import pandas as pd

##################################################



########## DEFINE
EXCEL_FILE_NAME = "data/car365_data.xlsx"
START_ROW_INDEX = 20
MAX_DATA_CNT = 100

##################################################



########## CLASS
class COL_INDEX(Enum):
    COMPANY = 0
    MODEL = 1
    FUEL = 2
    PURCHASED_COUNT = 3
    
    
    
class Origin():
    def __init__(self, origin):
        self.origin = origin
    
class Company(Origin):
    def __init__(self, origin, company):
        super().__init__(origin)
        self.company = company

class Car(Company):
    def __init__(self, origin, company, model, fuel):
        super().__init__(origin, company)
        self.model = model
        self.fuel = fuel

class Consumer(Car):
    def __init__(self, origin, company, model, fuel, age, pur_count):
        super().__init__(origin, company, model, fuel)
        self.age = age
        self.pur_count = pur_count
        
    def __str__(self):
        return f"origin={self.origin}, company={self.company}, model={self.model}, fuel={self.fuel}, age={self.age}, pur_count={self.pur_count}"

##################################################



########## VARIABLE
total_data = []

##################################################



########## MAIN
try:    
    excel_file = pd.ExcelFile(EXCEL_FILE_NAME)
    
    for sheet_name in excel_file.sheet_names:
        # print(sheet_name)
        df = pd.read_excel(EXCEL_FILE_NAME, sheet_name=sheet_name, engine="openpyxl")
        
        # 시트 이름에서 국산/수입 추출
        origin = -1
        if (sheet_name.startswith("국산")):
            origin = 0
        elif (sheet_name.startswith("수입")):
            origin = 1
        else:
            continue
        
        # 시트 이름에서 연령대 추출
        split_list = sheet_name.split('_')
        age = int(split_list[2][0:2])
        # print(age)
        
        for row_idx in range(START_ROW_INDEX, len(df) - 20):
            company = df.iloc[row_idx, COL_INDEX.COMPANY.value]
            if pd.isnull(company):
                break
            model = df.iloc[row_idx, COL_INDEX.MODEL.value]
            fuel = df.iloc[row_idx, COL_INDEX.FUEL.value]
            pur_count = df.iloc[row_idx, COL_INDEX.PURCHASED_COUNT.value]
        
            consumer = Consumer(origin=origin, company=company, model=model, fuel=fuel, age=age, pur_count=pur_count)
            total_data.append(consumer)
            
        print(f"'{sheet_name}' finished")
    
    print(f"total_data_len = {len(total_data)}")
    for data in total_data:        
        print(data)
    
except Exception as e:
    print(e)
    
finally:
    pass

##################################################