from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse

# ১. সার্চ টেক্সট ইউআরএল ফরম্যাটে কনভার্ট করা
search_query = "Sura Muminoon Ayat 84-87 shorts Yasser Al Dossari"
encoded_query = urllib.parse.quote(search_query)

# ২. ক্রোম অপশন কনফিগার করা (মজিলা ইউজার এজেন্ট যোগ করা)
options = webdriver.ChromeOptions()
mozilla_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"
options.add_argument(f"user-agent={mozilla_user_agent}")

# ৩. ড্রাইভার চালু করা
driver = webdriver.Chrome(options=options)

# ৪. সঠিক ইউআরএল-এ ভিজিট করা
driver.get(f"https://youtube.com{encoded_query}")

# ৫. এলিমেন্ট লোড হওয়া পর্যন্ত অপেক্ষা করা
wait = WebDriverWait(driver, 10)
first_video = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#video-title")))

# ৬. ভিডিওতে ক্লিক এবং মিনিমাইজ
first_video.click()
driver.minimize_window()