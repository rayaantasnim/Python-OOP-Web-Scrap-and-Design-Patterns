import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

url = "https://en.wikipedia.org/wiki/Bangladesh"
agent = {"User-Agent":"Mozilla/5.0"}

response = requests.get(url, headers=agent)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
a = soup.select("a")
data = []

for i in a:
    half_url = i.get("href")
    full_url = urljoin(url, half_url)
    data.append({
        "Source": i.text,
        "URL": full_url
    })

df = pd.DataFrame(data)
df.to_csv("Bangladesh.xlsx", index=False)