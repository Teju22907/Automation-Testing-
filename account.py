from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.get("https://footytips.com.au/")
time.sleep(10)

# driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/div/button[2]").click()
# time.sleep(3)



driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/div/button[1]").click()
time.sleep(3)

driver.switch_to.frame("oneid-iframe")

elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div/input")
time.sleep(8)
elem.send_keys("kalluriteju22@gmail.com")

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[3]/button").click()
time.sleep(5)

# driver.switch_to.default_content()

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[1]/div[1]/input").send_keys("Teja")
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div[1]/input").send_keys("Kalluri")
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[3]/div/input").send_keys("Tejaswini")
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[4]/div/div[1]/input").send_keys("narasinha@22")
time.sleep(5)

select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/form/label[1]/div/select'))
select.select_by_visible_text("Woman")
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/fieldset/div/div/input").send_keys(3148)
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/label[3]/input").click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/button").click()
time.sleep(5)

# driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/label[3]/input").click()
# time.sleep(5)