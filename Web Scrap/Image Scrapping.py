import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import os

url = "https://dreamersacademy.com.bd/"
agent = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=agent)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
image = soup.find_all("img")

folder = "dreamers_images"
os.makedirs(folder, exist_ok=True)

count = 0
images = []

for i in image:
    img_src = i.get("src")

    if img_src:
        full_url = urljoin(url, img_src)

    if not img_src:
        continue

    if img_src.startswith("data:") or img_src.endswith(".svg") or img_src.endswith(".gif"):
        continue

    img_response = requests.get(full_url, headers=agent)
    print(img_response.status_code)
    
    if img_response.status_code == 200:
        count += 1
        file_path = os.path.join(folder, f"image_{count}.jpg")
        
        with open(file_path, "wb") as f:
            f.write(img_response.content)

        images.append({
            "image_no": count,
            "image_url": full_url
        })

df = pd.DataFrame(images)
df.to_csv("image_data.csv", index=False)
print(f"Total images downloaded: {count}")