import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://books.toscrape.com/"
agent = {"User-Agent":"Mozilla/5.0"}

response = requests.get(url, headers=agent)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
div = soup.select(".image_container a")
data = []

for i in div:
    href = i.get("href")
    full_link = urljoin(url, href)
    data.append(full_link)

books = []
for link in data:
    r = requests.get(link, headers=agent)
    s = BeautifulSoup(r.text, "html.parser")

    title = s.select_one(".product_main h1").text.strip()
    price = s.select_one(".price_color").text.strip()
    availability = s.select_one(".instock.availability").text.strip()

    books.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

df_books = pd.DataFrame(books)
df_books.to_csv("Books.csv", index=False)