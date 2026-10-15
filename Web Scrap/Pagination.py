import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/page/"
agent = {"User-Agent":"Mozilla/5.0"}
data = []

for i in range(1,5):
    main_url = f"{url}{i}"
    response = requests.get(main_url, headers=agent)
    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.select(".quote")

for i in div:
    q = i.select_one(".text")
    a = i.select_one(".author")
    
    data.append({
        "Author": a.text,
        "Quote": q.text
    })

df = pd.DataFrame(data)
df.to_csv("Pagination.csv", index=False)