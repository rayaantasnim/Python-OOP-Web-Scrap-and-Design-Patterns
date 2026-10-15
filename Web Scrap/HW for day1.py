import requests
from bs4 import BeautifulSoup

url = "https://uniqueprogressiveschool.com/"
response = requests.get(url)
print(response.status_code)
#print(response.text) -> Just to see the code

soup = BeautifulSoup(response.text, "html.parser")
t = soup.find("title")
print(t.text)

p = soup.find_all("p")
for i in p:
    print(i.text)
    print("----------------")
    print("")

H1 = soup.find_all("h1")
for i in H1:
    print(i.text)
    print("-------------------")
    print("")

H2 = soup.find_all("h2")
for i in H2:
    print(i.text)
    print("-------------------")
    print("")

H3 = soup.find_all("h3")
for i in H3:
    print(i.text)
    print("-------------------")
    print("")

H4 = soup.find_all("h4")
for i in H4:
    print(i.text)
    print("-------------------")
    print("")

H5 = soup.find_all("h5")
for i in H5:
    print(i.text)
    print("-------------------")
    print("")

H6 = soup.find_all("h6")
for i in H6:
    print(i.text)
    print("-------------------")
    print("")

li = soup.find_all("li")
for i in li:
    print(i.text)
    print("----------")
    print("")