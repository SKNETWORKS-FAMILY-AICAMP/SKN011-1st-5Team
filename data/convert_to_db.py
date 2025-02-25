########## IMPORT
from enum import Enum
import pandas as pd
from car_class import *
##################################################



########## DEFINE
EXCEL_FILE_NAME = "./data/car365_data.xlsx"
START_ROW_INDEX = 20

##################################################



########## Enum
class COL_INDEX(Enum):
    COMPANY = 0
    MODEL = 1
    FUEL = 2
    PURCHASED_COUNT = 3

##################################################



########## FUNCTION
def return_Consumer_list(excel_file_full_path):
    total_data = []
    
    try:    
        excel_file = pd.ExcelFile(excel_file_full_path)
        
        for sheet_name in excel_file.sheet_names:
            # print(sheet_name)
            df = pd.read_excel(excel_file_full_path, sheet_name=sheet_name, engine="openpyxl")
            
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
            
            data_cnt = len(df) - START_ROW_INDEX
            for row_idx in range(START_ROW_INDEX, data_cnt):
                company = df.iloc[row_idx, COL_INDEX.COMPANY.value]
                if pd.isnull(company):
                    break
                model = df.iloc[row_idx, COL_INDEX.MODEL.value]
                fuel = df.iloc[row_idx, COL_INDEX.FUEL.value]
                pur_count = df.iloc[row_idx, COL_INDEX.PURCHASED_COUNT.value]
            
                consumer = Consumer(origin=origin, company=company, model=model, fuel=fuel, age=age, pur_count=pur_count)
                total_data.append(consumer)
                
            print(f"'{sheet_name}' finished")
        
        print(f"total_data count = {len(total_data)}")
        # for data in total_data:        
        #     print(data)
        
    except Exception as e:
        print(e)
        
    return total_data
##################################################