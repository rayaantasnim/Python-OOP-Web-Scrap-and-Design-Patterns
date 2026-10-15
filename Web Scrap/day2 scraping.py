import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
print(response.status_code)
#print(response.text) -> Just to see the code

soup = BeautifulSoup(response.text, "html.parser")

span = soup.select_one(".text") 
# -> To select just 1 pc
print(span.text)

#First option
quote = soup.select(".text")
# -> To select all the classes

author = soup.select(".author")
for a in quote:
    for b in author:
        # print(a.text) #->Just to see the quotes
        # print(b.text) #->Just to see the author name
        pass

#Second option
div = soup.select(".quote")
for i in div:
    q = i.select_one(".text")
    print(q.text)

    a = i.select_one(".author")
    print(a.text)
    print("------------------------")

    print("")