from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

def get_home_page():
    
    driver.get("https://footytips.com.au/")


def user_creation(email_address,first_name,last_name,display_name,password,gender,post_code):
    get_home_page()
    time.sleep(5)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/div/button[1]").click()
    time.sleep(5)
   
    driver.switch_to.frame("oneid-iframe")  
   
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div/input")
    time.sleep(5)
    elem.send_keys(email_address)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[3]/button").click()
    time.sleep(8)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[1]/div[1]/input").send_keys(first_name)
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div[1]/input").send_keys(last_name)
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[3]/div/input").send_keys(display_name)
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[4]/div/div[1]/input").send_keys(password)
    time.sleep(5)

    select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/form/label[1]/div/select'))
    select.select_by_visible_text(gender)
    time.sleep(5)
 
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/fieldset/div/div/input").send_keys(post_code)
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/label[3]/input").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/button").click()
    time.sleep(5)

def user_login(user_name,password):
    get_home_page()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/div/button[2]").click()
    time.sleep(5)


    driver.switch_to.frame("oneid-iframe")

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div/input")
    element.send_keys(user_name)

    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[3]/button").click()
    time.sleep(3)

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div/div/input")
    element.send_keys(password)
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[3]/div/button").click()
    time.sleep(5)

    driver.switch_to.default_content()
    time.sleep(5)

def user_update():

    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/input').send_keys("orange")
    time.sleep(5)
   
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/form/div/div[2]/div/input').send_keys("AFL")
    time.sleep(5)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/form/div/div[3]/div[1]/div[1]/label/span[1]').click()
    time.sleep(5)

    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/form/div/div[3]/div[2]/div/label/span[1]').click()
    time.sleep(5)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/form/div/div[3]/div[3]/div/label/span[1]').click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/form/div/div[3]/div[4]/div/label/span[1]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div/div/div/div[1]/form/button").click()
    time.sleep(5)

   

def update_display_name():

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/ul/li[4]/a").click()
    time.sleep(8)
    
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div[2]/div/form/div/div[1]/div[2]/div/div/input")
    elem.clear()
    elem.send_keys("Orange 2345")
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div[2]/div/form/div/div[6]/button").click()
    time.sleep(5)

def upload_tips():



    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/ul/li[3]/a").click()
    time.sleep(8)


    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div[1]/div/div/form/div/div/div[2]/div[1]/div').click()
    time.sleep(5)

    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/ul/li[2]').click()#NRL
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/form/div/div[1]/button").click()
    time.sleep(8)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/form/div/div[8]/div/div[1]/div[1]/div").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[14]").click()#Richmond
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/form/div/div[8]/div/div[1]/div[2]/div/div[1]/label/span[1]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/form/div/div[8]/div/div[1]/div[2]/div/div[2]/label/span[1]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/form/div/div[8]/div/div[1]/div[2]/div/div[3]/label/span[1]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/form/div/div[8]/div/div[1]/div[2]/div/div[4]/label/span[1]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/form/div/div[8]/div/div[1]/button").click()
    time.sleep(5)


def create_comp():

    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/ul/li[2]/a").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/p").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[1]/div/div/input").send_keys("jonny")
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div/div/input").send_keys("jonny3test")
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[7]/textarea").send_keys("jonnytest")
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[8]/button").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div/div[1]/label").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[11]/button[2]").click()
    time.sleep(8)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div[1]/div[1]/label/span[2]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[3]/button[2]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[3]/button[2]").click()
    time.sleep(5)

def join_comp():
    
   driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/div/div/div/button[2]/span").click()
   time.sleep(5)

   driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/form/div[1]/div/div/input").send_keys("Richmond")
   time.sleep(5)

   driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/form/div[1]/div/div/div[2]/div").click()
   time.sleep(5)

   driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/div/table/tbody[1]/tr/th/a/div").click()
   time.sleep(8)

   driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/div[2]/div/div/div[2]/div/form/div[1]/div/div/div/label[2]/span[2]").click()
   time.sleep(3)

   driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/div[2]/div/div/div[2]/div/form/div[2]/div/div/div/label[2]/span[2]").click()
   time.sleep(5)

   driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[5]/div/div[2]/div/div/div[2]/div/form/div[3]/div/button[2]/span").click()
   time.sleep(5)

#    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/div[1]/div/div/button[1]").click()
#    time.sleep(5)

#    driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[3]/div/button[2]/span").click()
#    time.sleep(5)

def invite_comp():

    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[2]/a/p").click()
    time.sleep(5)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/form/div[1]/div/div/div/input").send_keys("kalluriteju22@gmail.com")
    time.sleep(5)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/form/div[3]/textarea").send_keys("Welcome to ESPN")
    time.sleep(8)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/form/div[4]/button/span").click()
    time.sleep(8)

def new_create_comp():

    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[1]/ul/li[2]/a").click()
    time.sleep(5)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/p").click()
    time.sleep(5)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[1]/div/div/input").send_keys("Test2")
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div/div/input").send_keys("Test1")
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[8]/button").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div/div[1]/label").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div/div[2]/label").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[3]/div/div[2]/label").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[4]/div/div[1]/label").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[4]/div/div[2]/label").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[11]/button[2]/span").click()
    time.sleep(5)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div[1]/div[1]/label").click()
    time.sleep(3)


    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div[2]/div[1]/label").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div[3]/div[1]/label").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[3]/button[2]/span").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[2]/div/div/div/label[2]/span[2]").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[4]/button[2]/span").click()
    time.sleep(3)

def new_invite_comp():

    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[3]/div/div/div/div/div[2]/a/p").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/form/div[1]/div/div/div/input").send_keys("kalluriteju22@gmail.com")
    time.sleep(3)

    ele = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/form/div[3]/textarea")
    ele.clear()
    ele.send_keys("Welcome to ESPN")
    time.sleep(3)


    driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[4]/div/form/div[4]/button/span").click()
    time.sleep(3)

    # driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[4]/button[2]/span").click()
    # time.sleep(3)

    # driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[4]/button[2]/span").click()
    # time.sleep(3)

    




    # driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[4]/div/div[2]/label/span[1]/input").click()
    # time.sleep(3)

    # driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div[2]/div/div/form/div[4]/div/div[2]/label/span[1]/input").click()
    # time.sleep(3)

    







def main():
     #user_creation("kamepallianitha23@gmail.com","anitha","kamepalli","anitha","anitha@123","Woman",3148)
    user_login("kalluritejaswini334@gmail.com","Tejaswini@123")
    #update_display_name()
    #user_update()
    #upload_tips()
    # create_comp()
    # join_comp()
    # invite_comp()
    # new_create_comp()
    new_invite_comp()


main()

