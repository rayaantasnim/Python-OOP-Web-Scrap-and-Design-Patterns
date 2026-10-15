import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.goodreads.com/quotes?page="
agent = {"User-Agent":"Mozilla/5.0"}
data = []

for i in range(1,5):
    main_url = f"{url}{i}"
    response = requests.get(main_url, headers=agent)
    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.select(".quoteText")
    for i in div:
        a = i.select_one(".authorOrTitle")
        
        data.append({
            "Quote": i.text.strip(),
            "Author": a.text.strip()
        })

df = pd.DataFrame(data)
df.to_csv("Pagination HW Quotes.csv", index=False)