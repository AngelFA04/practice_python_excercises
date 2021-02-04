import requests
from bs4 import BeautifulSoup


URL = "https://www.nytimes.com/international/"

def get_page_parsed(url):
    """
    Return the page as a Soup.
    """
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("There was an error!")

    return BeautifulSoup(response.text, features="lxml")

def parse_titles(soup):
    titles = soup.find_all("h2", attrs={"class":"css-1sk5x1x e1voiwgp0"})
    titles.extend(soup.find_all("span", attrs={"class":"balancedHeadline"}))
    titles.extend(soup.find_all("h2", attrs={"class":"css-l8hvcb e1voiwgp0"}))
    titles.extend(soup.find_all("h3", attrs={"class":"css-codfme e1lsht870"}))

    titles = [title.text for title in titles]

    return titles


if __name__ == "__main__":
    soup = get_page_parsed(URL)

    for title in parse_titles(soup):
        print("-", title)
