import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    response = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
    if response.status_code != 200:
        raise Exception("This article was not downloades properly.")


    soup = BeautifulSoup(response.text,features="lxml")
    paragraphs = soup.find("article").find("div", class_="content-background").find("div").find("div", class_="article__chunks"
).find_all("p")

    for p in paragraphs:
        print(p.text)
