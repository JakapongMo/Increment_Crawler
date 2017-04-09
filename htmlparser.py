import sys
from bs4 import BeautifulSoup
#from nltk.corpus import stopwords
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

def wordcount(text):
    wordcount={}
    count= 0
    for word in text.split():
        if word not in wordcount:
            wordcount[word] = 1
            count += 1
        else:
            wordcount[word] += 1
            count += 1
    print (word,wordcount)
    return count



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
count = wordcount(soup.title.string)

text = soup.get_text()
new_text = ''
for char in text:
    if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >=97 and ord(char) <=122) or ord(char)==40 or ord(char) ==10 or ord(char)==32) or (ord(char) >= 48 and ord(char) <= 57):
        new_text += char

#print (new_text)
count = wordcount(new_text)
count_title = wordcount(soup.title.string)
print ("word_count_title :", count_title)
print ("word_count_body :", count- count_title)
