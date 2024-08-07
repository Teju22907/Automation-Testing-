from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/search")
time.sleep(5)



driver.find_element(By.XPATH("//h3[contains(text(),'Amazon.com.au: Shop online for Electronics, Appare')]")).Click()

# driver.findElement(By.xpath("//img[@alt='Everything for your home']"))
# driver.findElement(By.xpath("//input[@data-action-params='{"toasterType":"AEE_AUTO_DETECTED_LOCATION"}']"))
# driver.findElement(By.xpath("//input[@data-action-params='{"toasterType":"AEE_AUTO_DETECTED_LOCATION"}']"))
# driver.findElement(By.xpath("//div[normalize-space()='EN']"))
# driver.findElement(By.xpath("//span[@id='glow-ingress-line1']"))
# driver.findElement(By.xpath("//input[@id='GLUXPostalCodeWithCity_PostalCodeInput']"))
# driver.findElement(By.xpath("//span[@id='GLUXPostalCodeWithCity_DropdownButton']//span[@role='radiogroup']"))
# driver.findElement(By.xpath("//a[@id='GLUXPostalCodeWithCity_DropdownList_0']"))
# driver.findElement(By.xpath("//span[@id='GLUXPostalCodeWithCityApplyButton']//input[@type='submit']"))
# driver.findElement(By.xpath("//form[@id='international-customer-select-preferences-form']"))