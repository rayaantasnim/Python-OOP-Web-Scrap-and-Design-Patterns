import requests
from bs4 import BeautifulSoup

url = "https://dreamersacademy.com.bd/"
response = requests.get(url)
print(response.status_code)
#print(response.text) -> Just to see the code

soup = BeautifulSoup(response.text, "html.parser")
t = soup.find("title")

print (t)
#-> Programming Language

print(t.text)
#-> Natural Language

L = soup.find_all("p")
for i in L:
    print(i.text)
    print("----------------")
    print("")