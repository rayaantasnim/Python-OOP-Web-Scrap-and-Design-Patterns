import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

#print(response.status_code) -> To see the allowance for scrapping
#print(response.text) -> Just to see the code
soup = BeautifulSoup(response.text, "html.parser")

div = soup.select(".quote")
for i in div:
    q = i.select_one(".text")
    print(q.text)

    a = i.select_one(".author")
    print(a.text)
    
    t = i.select(".tag")
    print("")
    for a in t:
        print(a.text)

    print("------------------------")
    print("")
    print("")