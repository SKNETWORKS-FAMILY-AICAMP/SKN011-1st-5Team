import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def crawl_hyundai():
    # 크롬 드라이버 실행행
    path = 'chromedriver.exe'
    service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome()

    driver.get('https://www.hyundai.com/kr/ko/e/customer/center/faq')
    time.sleep(1)

    questions = []
    answers = []

    for page in range(1,5):
        print(f" 현재 {page}페이지 크롤링 중...")
        items = driver.find_elements(By.CSS_SELECTOR, 'div.list-wrap')

        text_list = [item.text for item in items]
        # print(text_list)


        for text in text_list:
            questions.extend(text.split('\n')) 

        print('버튼 찾기 성공공')

        btns = driver.find_elements(By.CSS_SELECTOR, 'div.list-item')

        for i, btn in enumerate(btns):
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", btn)
            time.sleep(1.5) 

            btn.click()
            time.sleep(1)

            answer = driver.find_element(By.CSS_SELECTOR, 'div.conts')
            answers.append(answer.text)
        
        if page < 4:
            next_page_xpath = f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[2]/div/ul/li[{page+1}]'

            next_page_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_page_xpath)))

            # 스크롤 이동 및 대기기
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_page_btn)
            time.sleep(1.5) 

            next_page_btn.click()
            time.sleep(1)

    # 짝수 인덱스를 삭제
    for i in range(len(questions)-1, -1, -1): 
        if i % 2 == 0:
            del questions[i]

    faq_hd = dict(zip(questions, answers))

    with open('../data/faq_hd.json','w',encoding='utf-8') as f:
        json.dump(faq_hd, f, ensure_ascii=False, indent=4)

    print(json.dumps(faq_hd, ensure_ascii=False, indent=4))


    # for i in range(len(answers)):
    #     print(f'Q{i}: {questions[i]}\nA{i}: {answers[i]}\n')
    #     print()

    

