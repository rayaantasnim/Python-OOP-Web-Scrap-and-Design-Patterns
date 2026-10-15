import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url) 

# print(response.status_code) -> To see the allowance for scrapping
# print(response.text) -> Just to see the code
soup = BeautifulSoup(response.text, "html.parser")

div = soup.select(".quote")
data = []

for i in div:
    q = i.select_one(".text")
    a = i.select_one(".author")
    
    data.append({
        "Author": a.text,
        "Quote": q.text
    })

for i in data:
    print(i)

df = pd.DataFrame(data)
df.to_csv("Quotes.csv", index=False)