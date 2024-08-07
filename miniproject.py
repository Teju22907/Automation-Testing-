from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller # type: ignore
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
 
def homepage():
     
     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def test_login():
    homepage()
    time.sleep(3)

    element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    element.send_keys('kajal')

    time.sleep(3)

    element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    element.send_keys('Narasimha@123')
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    time.sleep(5)



# def test_admin():
#     test_login()                                                           
#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
#     time.sleep(3)
    
#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
#     time.sleep(5)

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul").click()
#     time.sleep(5)

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
#     time.sleep(3)

#     driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()

#     element1 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input")
#     element1.clear()
#     element1.send_keys("Pandu")
#     time.sleep(3)

#     element2 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")
#     element2.clear()
#     element2.send_keys("chanti")
#     time.sleep(3)

#     element3 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
#     element3.clear()
#     element3.send_keys("jonny@123")
#     time.sleep(3)

#     element4 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
#     element4.clear()
#     element4.send_keys("jonny@123")
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]").click()
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[3]/span[1]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[3]/ul[1]/li[1]/a[1]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]").click()
#     time.sleep(3)
#     element5 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
#     element5.clear()
#     element5.send_keys("OrangeHRM")
#     time.sleep(3)
#     element6 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")
#     element6.clear()
#     element6.send_keys("12345")
#     time.sleep(3)
#     ele7 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]") 
#     ele7.clear()
#     ele7.send_keys("567866")
#     time.sleep(3)
#     ele8 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]")
#     ele8.clear()
#     ele8.send_keys("01234567")
#     time.sleep(3)
#     ele9 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/input[1]")
#     ele9.clear()
#     ele9.send_keys("8019")
#     time.sleep(3)
#     ele10 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[3]/div[1]/div[2]/input[1]")
#     ele10.clear()
#     ele10.send_keys("info@orangehrm.com")
#     time.sleep(3)
#     ele11 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]") 
#     ele11.clear()
#     ele11.send_keys("538 Teal Plaza")
#     time.sleep(3)
#     ele12 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/input[1]")
#     ele12.clear()
#     ele12.send_keys("Mysore")
#     time.sleep(3)
#     ele13 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[3]/div[1]/div[2]/input[1]")
#     ele13.clear()
#     ele13.send_keys("Secaucus")
#     time.sleep(3)
#     ele14 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[3]/div[1]/div[2]/input[1]")
#     ele14.clear()
#     ele14.send_keys("UMI")
#     time.sleep(3)
#     ele15 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[5]/div[1]/div[2]/div[1]/div[2]/input[1]")
#     ele15.clear()
#     ele15.send_keys("51217")
#     time.sleep(3)
#     ele16 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[3]/div[1]/div[2]/input[1]")
#     ele16.clear()
#     ele16.send_keys("Secaucus")
#     time.sleep(3)
#     ele17 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[6]/div[1]/div[1]/div[2]/textarea[1]")
#     ele17.clear()
#     ele17.send_keys("HRM Software")
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[7]/button[1]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[6]/a[1]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/button[3]").click()
   


# def test_PIM():
#     test_admin()

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click()
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("Test")
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys("06619")
#     time.sleep(3)

#     driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Tester")
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/input[1]").send_keys("Sample")
#     time.sleep(3)

#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Narasimha@123")
#     time.sleep(3)
#     #username
#     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("Narasimha@123")
#     time.sleep(3)
#     # password
#     driver.find_element(By.XPATH, "//button[@type='submit']").click()
#     time.sleep(3)


#     driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]").click()
#     time.sleep(3)

    

def test_leave():
    test_login()

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
    time.sleep(3)

    # driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-up-fill oxd-select-text--arrow']").click()
    # time.sleep(3)

    # driver.find_element(By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//i[1]").click()
    # time.sleep(3)

    # driver.find_element(By.XPATH, "//div[@class='--holiday-full oxd-calendar-date'][normalize-space()='4']").click()
    # time.sleep(3)

    # driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").click()
    # time.sleep(3)

    # driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
    # time.sleep(3)



    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click()
    time.sleep(3)
    
     
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]").click()
    time.sleep(3)



def test_time():
    test_leave()
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[normalize-space()='Edit']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[3]/div/div[2]/input").click()
    time.sleep(3)
    input_field = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[3]/div/div[2]/input")
    input_field.send_keys("8")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[2]/input[1]").send_keys(8)
    time.sleep(3)
    
 
def test_recritment():
    test_time() 

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click()
    time.sleep(3)


def test_myinfo():

    test_recritment()

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("Kajal")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/input[1]").send_keys("Actor")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("12345")
    time.sleep(3)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]").send_keys("56789")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/i[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/label[1]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("2220")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    time.sleep(3)
    # driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]").click()
    # time.sleep(3)

    keyboard = Controller()

    keyboard.type("C:\\Users\\vamsi\\Downloads\\Testcase Template")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[3]/button[2]").click()
    time.sleep(3)
    # driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]").click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]").click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]").click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]").click()
    # time.sleep(3)



def test_performance():
    test_myinfo()

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[7]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/span[1]/i[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/ul[1]/li[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Tester")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Peter Mac Anderson")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[3]/a[1]").click()
    time.sleep(3)


def test_Dashboard():
    test_performance()

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[8]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/i[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/i[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[3]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[4]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys("pandu")
    time.sleep(3)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]").click()
    time.sleep(3)



def test_directory():
    test_Dashboard()

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[9]/a[1]/span[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Test  Sample")
    time.sleep(3)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
    time.sleep(3) 

def test_maintanence():
    test_directory()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[10]/a[1]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/input[1]").send_keys("admin123")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/div[4]/button[2]").click()
    time.sleep(3)

def test_claim():
    test_maintanence()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[11]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/ul[1]/li[1]").click()
    time.sleep(3)

def test_buzz():
     test_claim()
     driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[12]/a[1]").click()
     time.sleep(3)
    #  driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]").click()
    #  time.sleep(3)

    #  driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/textarea[1]").send_keys("Hello all, Welcome to Orange HRM")
    #  time.sleep(3)
     
test_buzz()    