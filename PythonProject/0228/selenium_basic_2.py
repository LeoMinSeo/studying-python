import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)

# 헤드리스 모드 설정
chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저 창 숨김
chrome_options.add_argument('--disable-gpu')  # GPU 가속 비활성화 (일부 시스템에서 필요)
chrome_options.add_argument('--no-sandbox')  # 샌드박스 비활성화 (리눅스 서버에서 필요할 수 있음)
chrome_options.add_argument('--disable-dev-shm-usage')  # 공유 메모리 사용 방식 변경 (리눅스 서버에서 도움됨)

# 셀레니움 드라이버 설정
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(15)

# 언어 감지 함수
def is_korean(text):
    # 한글 포함 여부 확인 (가-힣)
    return bool(re.search(r'[가-힣]', text))

def is_english(text):
    # 영어 문자, 숫자, 공백, 기본 구두점만 포함 여부 확인
    return bool(re.match(r'^[A-Za-z0-9\s.,!?;:\'"-]+$', text))

def detect_language(text):
    if is_korean(text):
        return "ko"
    elif is_english(text):
        return "en"
    else:
        # 다른 언어이거나 혼합된 경우 기본값
        return "en"


@app.route('/datapost', methods=['POST'])
def get_data():
    try:
        # 네이버 접속
        driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%ED%8C%8C%EA%B3%A0&ackey=olqw5zwv")

        # 요청 데이터 가져오기
        data = request.get_json()
        wantTrans = data
        print("post:", wantTrans)

        # 언어 감지
        detected_lang = detect_language(wantTrans)
        print(f"감지된 언어: {detected_lang}")

        # 언어 감지 결과에 따라 처리
        if detected_lang == "en":
            # 영어가 감지된 경우 언어 전환 버튼 클릭
            try:
                # 언어 전환 버튼 클릭
                lang_switch_btn = driver.find_element(By.XPATH, '//*[@id="_au_translator"]/div/div[1]/div[2]/div[2]/a')
                lang_switch_btn.click()
                print("언어 전환 버튼 클릭됨")
                time.sleep(0.5)  # 언어 전환 후 잠시 대기
            except Exception as e:
                print(f"언어 전환 버튼 클릭 중 오류: {str(e)}")

        # 번역할 텍스트 입력
        entry1 = driver.find_element(By.XPATH,
                                     '//*[@id="_au_translator"]/div/div[1]/div[2]/div[2]/div[1]/div[2]/textarea[1]')
        entry1.clear()  # 기존 텍스트 지우기
        entry1.send_keys(wantTrans)

        # 번역 버튼 클릭
        clicks = driver.find_element(By.XPATH, '//*[@id="_au_translator"]/div/div[1]/div[2]/div[2]/div[1]/div[3]/a[4]')
        clicks.send_keys(Keys.ENTER)

        # 번역 결과 가져오기 전 대기
        time.sleep(1)

        # 번역 결과 가져오기
        datas = driver.find_element(By.XPATH, '//*[@id="_au_translator"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/p')
        results = datas.text
        print("번역 결과:", results)

        return jsonify({"result": results})

    except Exception as e:
        print("오류 발생:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)