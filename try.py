import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://staging.profoam.com/checkout/cu-6-dynasolve-1-gallon-185")

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//label[@for= '1228']").click()
driver.find_element(By.XPATH,"//input[@name= 'shipping_method_sp']").click()
driver.find_element(By.XPATH,"//input[@name= 'shipping_method_ups']").click()
driver.find_element(By.XPATH,"//span[@class= 'radio_class']").click()
driver.find_element(By.XPATH,"//input[@data-elements-stable-field-name= 'cardNumber']").send_keys("424242424242")
time.sleep(3)
