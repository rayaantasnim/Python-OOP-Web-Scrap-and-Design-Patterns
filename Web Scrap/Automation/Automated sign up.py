from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/register")
f_name = driver.find_element(By.ID, "firstname")
f_name.send_keys("ABC")

l_name = driver.find_element(By.ID, "lastname")
l_name.send_keys("XYZ")

username = driver.find_element(By.ID, "userName")
username.send_keys("abcxyz")

password = driver.find_element(By.ID, "password")
password.send_keys("Abc@123!")

button = driver.find_element(By.ID, "register")
button.click()

time.sleep(120)
driver.quit()