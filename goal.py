from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get('https://www.goal.com/en-au')
time.sleep(5)

def account_creation():
    driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[3]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/p/a/span').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/button[1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/form/div[1]/label/input').send_keys('kalluritejaswini334@gmail.com')
    time.sleep(5)

    driver.find_element(By.NAME,'password').send_keys('VamsiTeju@26')
    time.sleep(5)
    driver.find_element(By.NAME,'repeatedPassword').send_keys('VamsiTeju@26')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/form/label/div').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/form/button').click()
    time.sleep(5)

account_creation()

def loginlogout():
    driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[3]').click()
    time.sleep(5)
    driver.find_element(By.NAME,'email').send_keys('kalluriteju22@gmail.com')
    time.sleep(5)
    driver.find_element(By.NAME,'password').send_keys('Narasimha@22')
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div/form/button').click()
    time.sleep(5)

    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div/form/button').click()
    time.sleep(5)

    driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/div/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/button[1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/form/label[1]').send_keys('Teju')
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/form/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/button[3]').click()
    time.sleep(5)


loginlogout()    

    
   
