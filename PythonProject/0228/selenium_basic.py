import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.implicitly_wait(15)#묵시적 대기, 활성화 를 최대 15초까지 기다린다

#전체화면모드로 변경
driver.fullscreen_window()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.set_window_rect(100,100,500,500)#특정 좌표와크기로 변경
time.sleep(2)
driver.get("http://selenium.dev")
# 5초후 종료
time.sleep(5)
driver.close()