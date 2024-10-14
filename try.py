import time
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.chekout import Checkout
from utilities.logger import BaseClass





driver = webdriver.Chrome()

driver.get("https://profoam.com/pf-accufoam-17-hfc-foam")
driver.maximize_window()
driver.implicitly_wait(10)

# time.sleep(10)  # Consider removing or reducing this wait

shadow_host = driver.find_element(By.CSS_SELECTOR, "chat-widget[location-id='ezamnLIXmzsU7b44Ya21']")
shadow_root = shadow_host.shadow_root  # Access the shadow root directly
close_button = shadow_root.find_element(By.CSS_SELECTOR, "button.lc_text-widget_prompt--prompt-close")
close_button.click()
# try:
#     # Find all SVG elements with the specified ID
#     svg_elements = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.XPATH, "//*[local-name()='svg' and @id='Capa_1']"))
#     )
#
#     # Click on the first SVG element if it exists
#     if svg_elements:
#         for element in svg_elements:
#             try:
#                 # Wait until the element is clickable
#                 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[local-name()='svg' and @id='Capa_1']")))
#
#                 # Scroll into view
#                 driver.execute_script("arguments[0].scrollIntoView();", element)
#
#                 # Now try clicking
#                 element.click()
#                 print("Click Successful")
#                 break  # Exit loop after clicking
#             except ElementClickInterceptedException:
#                 print("Element not clickable due to another element overlaying it.")
#             except Exception as click_exception:
#                 print(f"Error clicking the SVG element: {click_exception}")
#     else:
#         print("No SVG elements found.")
#
# except TimeoutException:
#     print("Timed out waiting for SVG elements to be present.")
# except NoSuchElementException:
#     print("SVG elements not found in the DOM.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
#
# driver.quit()

elements = driver.find_elements(By.XPATH,"//*[local-name()='svg' and @id='Capa_1']")
for element in elements:
    element.click()
    print("Click Successful")
    break