"""
Script to automatize the process of creating the folder,
markdown and main.py pf each problem."""

import os
import requests
from lxml import html
from concurrent.futures import ThreadPoolExecutor

XPATH_LINKS =  '//div[@class="left"]//a/@href'


def get_page_parsed(link):
    """Get the content page and return a string"""
    response = requests.get(link).content.decode('utf-8')
    text_parsed = html.fromstring(response)

    return text_parsed


def get_links(link, xpath_expression):
    """Get a list of links"""
    home = get_page_parsed(link)

    return home.xpath(xpath_expression)


def get_page_content(link):
    """Get all the data needed from each exercise page."""
    content = dict()
    pass
    page = get_page_parsed(link)

    content['title'] = page.xpath('//h1[@class="pagetitle"]/text()')[0].strip()

    # content['body'] = page.xpath('//p/*')[0].text
    # content['body'] = page.xpath('//p/text()')[0].text

    # Get the paragraphs below to h2 title with content having the word "Excercise"

    # All the text between Excercise and Discussion
    #page.xpath('//div[@class="boxframe center"]/span/h2[contains(@id, "exercise")]/following-sibling::p').xpath('.//text()')

    nodes = page.xpath('//div[@class="boxframe center"]/span/h2[contains(@id, "exercise")]/following-sibling::*')
    paragraphs = []
    # Iterate while tag is 'p'
    for n in nodes:
        if n.tag == 'p':
            paragraphs.append(n)
        elif n.tag == 'h2':
            break

    paragraphs = [' '.join(p.xpath('.//text()')) for p in paragraphs]

    content['body'] = {f'{p}\n' for p in paragraphs}

    content['link'] = link

    import pdb; pdb.set_trace()
    return content


def create_markdown_file(i, content):

    os.mkdir(f'./excercise_{i}')
    with open(f'./excercise_{i}/README.md', 'w') as fp:
        # Append title
        fp.write(f"\n# {i} - {content['title']}\n")
        # Add link
        fp.write(f"\n[Excercise link]({content['link']})\n\n")
        # Append problem description
        {fp.write(p) for p in content['body']}

    with open(f'./excercise_{i}/main.py', 'w') as fp:
        fp.write('')


def main(links):

    # Create each markdown from each link
    # Iterate in that range of links

    # Add concurrency here
    for i, link in enumerate(links[11:37], 11):
        content = get_page_content(link)
        create_markdown_file(i, content)


if __name__ == "__main__":
    # Get links
    main_link = "https://www.practicepython.org"
    links = get_links(main_link, XPATH_LINKS)
    links = [f'{main_link}{l}' for l in links]

    print(links)

    # Create each markdown from each link
    main(links)
