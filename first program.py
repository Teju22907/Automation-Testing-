from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get("https://footytips.com.au/")
time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/div/button[2]").click()
time.sleep(3)

# element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div/input')
# time.sleep(3)
# element.send_keys('vamsi.raavi123@gmail.com')

driver.switch_to.frame("oneid-iframe")

element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div/input")
element.send_keys('vamsi.raavi123@gmail.com')
time.sleep(3)


# driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div/input").send_keys("vamsi.raavi123@gmail.com")
# time.sleep(3)


driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[3]/button").click()
time.sleep(3)

elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[2]/div/div/input")
time.sleep(3)
elem.send_keys("Vamsikrishna@123")

driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/form/div[3]/div/button").click()
time.sleep(3)

driver.switch_to.default_content()

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/ul/li[4]').click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[3]/div/div/div/div[2]/div/form/div/div[6]/button").click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/a/p").click()
time.sleep(5)

# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# driver.close()