from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

search_box = driver.find_element(By.NAME, "search_query")
num = input("Enter what you want to search on YouTube: ")
search_box.send_keys(num)
search_box.send_keys(Keys.RETURN)

time.sleep(3)
data = []
videos = driver.find_elements(By.ID, "video-title")

for video in videos[:10]:
    a = video.text
    b = video.get_attribute("href")
    data.append({
        "Title": a,
        "URL": b
    })

driver.quit()

df = pd.DataFrame(data)
df.to_csv("YouTube.csv", index=False)

for i in data:
    print(i)