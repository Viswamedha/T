
import requests

# get

# 1st parameter - url
query = input()
url = "https://en.wikipedia.org/wiki/"+query
response = requests.get(url)

# beautiful soup
# checking html documents using python

# bs4
from bs4 import BeautifulSoup

# BeautifulSoup - class 
'''
class BeautifulSoup:
    def __init__(self, text, type):

        pass

    def find_all(self, html_attribute):

        return None

'''
r = requests.get(url)
soup = bs(r.content, 'lxml')
text = '\n'.join([i.text for i in soup.select('p')])
with open('newfile.txt',"w", encoding='utf-8') as file: file.write(text)
'''
soup = BeautifulSoup(response.text, 'html.parser')
# <a> </a>
urls = []
for link in soup.find_all('p'):
    urls.append(link.get(''))


'''


