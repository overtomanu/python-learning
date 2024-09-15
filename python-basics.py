import csv
import os
import textwrap
import shutil
import requests
import bs4
import timeit
import tempfile
import sys

# strings, comma prints space
print("Hello" , "world")

# int and float
print(42 , 3.1416)

# list
print([5,3,4,1])

# set, 2 is printed only once
print({2,3,2})

# map
print({"k1":"v1",3:54,"k1":"v2"})

# tuple
print(("string value",5,3,4,1))

# pyright gives error as type annotation is declared for str but int value is assigned
# code executes fine though
programming_language: str = 'Python'
programming_language=1
print(programming_language)

# lambda functions in python
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

print(map(square,my_nums))

# map in multiple line
d = {
    'k1':123,
    'k2':[0,1,2],
    'k3':{
        'insideKey':100
        }
    }
print(f"d - {d}")

help(timeit.timeit)
print(f"tempfile.gettempdir() = {tempfile.gettempdir()}")
print(f"os.path.join('usr','bin','spam') = {os.path.join('usr','bin','spam')}")


# paths
current_directory = os.getcwd()
print("os.getcwd() => ", os.getcwd())
os.chdir("../")
print('os.getcwd() after os.chdir("../")=> ', os.getcwd())
os.chdir(current_directory)
print("os.path.dirname(os.path.realpath(__file__)) => ", os.path.dirname(os.path.realpath(__file__)))
print("sys.path[0] => ", sys.path[0])
print("os.path.dirname(os.path.realpath(sys.argv[0])) => ", os.path.dirname(os.path.realpath(sys.argv[0])))
print("os.path.abspath('') => ", os.path.abspath(''))
print("os.environ['HOME'] => ", os.environ['HOME'])


# scraping
quotes_site_response = requests.request(url='http://quotes.toscrape.com/',method='GET')
#print(f"quotes_site_text => {str(quotes_site_response.text)}")
quotes_site_text = quotes_site_response.text
soup = bs4.BeautifulSoup(quotes_site_text,features="lxml")
authors_soup = soup.select(".author")
#print(f"authors_soup = {authors_soup}")
authors = {author.getText() for author in authors_soup}
print("authors => ", authors)

quotes_result_set = soup.select("div.quote > span.text")
quotes = {quote.get_text() for quote in quotes_result_set}
print("quotes => ", quotes)

top_tags_result_set = soup.select("div.tags-box .tag")
top_tags = {tag.get_text() for tag in top_tags_result_set}
print("top_tags => ", top_tags)

authors=set()
page_number = 1
while(True):
    try:
        print("getting authors from page ",page_number)
        quotes_site_response = requests.request(url=f'http://quotes.toscrape.com/page/{page_number}/',method='GET')
        quotes_site_text = quotes_site_response.text
        soup = bs4.BeautifulSoup(quotes_site_text,features="lxml")
        authors_result = soup.select(".author")
        if not authors_result:
            break
        for author in authors_result:
            authors.add(author.get_text())
        page_number += 1
    except Exception as e:
        print("caught exception e => ", e)
        break
print("authors => ", authors)
