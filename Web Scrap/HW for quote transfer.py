import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.goodreads.com/quotes"
agent = {"User-Agent":"Mozilla/5.0"}

response = requests.get(url, headers=agent)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
div = soup.select(".quoteText")
data = []

for i in div:
    a = i.select_one(".authorOrTitle")
    author = a.text.strip()
    quote = i.text.strip()

    data.append({
        "Author": author,
        "Quote": quote
    })

df = pd.DataFrame(data)
df.to_csv("HW.csv", index=False)