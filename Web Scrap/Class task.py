from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.minimize_window()

url = "https://realpython.github.io/fake-jobs/"
driver.get(url)
second = driver.find_elements(By.XPATH, "//a[text()='Apply']")
data = []

for i in second:
    sub = i.get_attribute("href")
    data.append(sub)

jobs = []
for item in data[:5]:
    driver.get(item)
    time.sleep(5)

    designation = driver.find_element(By.CSS_SELECTOR, ".title.is-2").text
    description = driver.find_element(By.XPATH, "//div[@class='content']/p[1]").text
    location = driver.find_element(By.ID, "location").text
    post = driver.find_element(By.ID, "date").text

    jobs.append({
        "Designation": designation,
        "Description": description,
        "Location": location,
        "Posted": post
    })

driver.quit()
df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False)