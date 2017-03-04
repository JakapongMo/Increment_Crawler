import sys
from bs4 import BeautifulSoup
'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    data = ''
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)
        data += data
        return data

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
'''

#########################################################
f = open('/home/tengmo/workwithcrawler/2000file/sub_testcrawl[116].arc', 'r')
text = ''
cnt = 0
for line in f:
    cnt +=1
    if(cnt>7):
        text += line
html_content = text
#########################################################

soup = BeautifulSoup(html_content, 'lxml')
soup.find_all('a')
print(soup.title.string)
list_link = (soup.find_all('a'))
list_table = (soup.find_all('table'))
list_picture = (soup.find_all('img'))
print ('Nb of link: ',len(list_link))
print('Nb of table',len(list_table))
print('Nb of picture',len(list_picture))
