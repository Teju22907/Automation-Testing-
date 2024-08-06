from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')

def login():
    driver.find_element(By.NAME,'email').send_keys('emailvamsi.raavi123@gmail.com')
    time.sleep(5)
    driver.find_element(By.NAME,'pass').send_keys('Vamsikrishna')
    time.sleep(5)
    driver.find_element(By.NAME,'login').click()
    time.sleep(10)

login()    