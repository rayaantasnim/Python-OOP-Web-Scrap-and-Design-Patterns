from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome ব্রাউজার চালু করা
driver = webdriver.Chrome()

# নির্দিষ্ট ওয়েবসাইটে যাওয়া
driver.get("https://the-internet.herokuapp.com/download")

# পেজ লোড হওয়ার জন্য অপেক্ষা
time.sleep(10)

# নির্দিষ্ট PDF ফাইলের লিঙ্ক খুঁজে বের করা
download_link = driver.find_element(By.LINK_TEXT, "testing_firefox.pdf")

# লিঙ্কে ক্লিক করে ডাউনলোড শুরু করা
download_link.click()

# ডাউনলোড সম্পূর্ণ হওয়ার জন্য অপেক্ষা
time.sleep(5)

# ব্রাউজার বন্ধ করা
driver.quit()
