from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.duckduckgo.com/")

search_box = driver.find_element(By.NAME, "q")
num = input("Enter what you want to search: ")

search_box.send_keys(num)
search_box.send_keys(Keys.RETURN)

time.sleep(10)

data = []
titles = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")
for title in titles:
    a = title.text
    b = title.get_attribute("href")
    data.append({"Title": a, "URL": b})

driver.quit()

df = pd.DataFrame(data)
df.to_csv("Python.csv", index=False)

print("Saved to Python.csv")
for i in data:
    print(i["Title"])
    print("=>")
    print(i["URL"])
    print("")