import requests
from bs4 import BeautifulSoup

def insert_paragraphs_in_file(file_name):
    response = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
    if response.status_code != 200:
        raise Exception("This article was not downloades properly.")


    soup = BeautifulSoup(response.text,features="lxml")
    paragraphs = (soup.find("article")
                .find("div", class_="content-background")
                .find("div")
                .find("div", class_="article__chunks")
                .find_all("p"))

    output_text = ""
    for p in paragraphs:
        output_text += p.text

    with open(file_name, mode="w") as f:
        f.write(output_text)

    print(f"Article saved in {file_name}")

if __name__ == '__main__':
    file_name = input("Insert the file name to save the article: ")
    insert_paragraphs_in_file(file_name)
