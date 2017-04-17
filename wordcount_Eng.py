import sys
from bs4 import BeautifulSoup

def wordcount(text):
    stopword = ['all', "she'll", 'just', "don't", 'being', 'over', 'through',
    		   'yourselves', 'its', 'before', "he's", "when's", "we've", 'had',
    			'should', "he'd", 'to', 'only', "there's", 'those', 'under',
    			'ours', 'has', "haven't", 'do', 'them', 'his', "they'll", 'get',
    			'very', "who's", "they'd", 'cannot', "you've", 'they', 'not',
    			'during', 'yourself', 'him', 'nor', "we'll", 'like', 'did',
    			"they've", 'this', 'she', 'each', "won't", 'where', "mustn't",
    			"isn't", "i'll", "why's", 'www', 'because', "you'd", 'doing',
    			'some', 'up', 'are', 'further', 'ourselves', 'out', 'what',
    			'for', 'while', "wasn't", 'does', "shouldn't", 'above', 'between',
    			'ever', 'ought', 'be', 'we', 'who', "you're", 'were', 'here',
    			'hers', "aren't", 'by', 'both', 'about', 'would', 'of', 'could',
    			'against', "i'd", "weren't", "i'm", 'com', 'or', "can't", 'own',
    			'into', 'whom', 'down', "hadn't", "couldn't", "wouldn't", 'your',
    			"doesn't", 'from', "how's", 'her', 'their', "it's", 'there',
    			'been', 'why', 'few', 'too', 'themselves', 'was', 'until', 'more',
    			'himself', "where's", "i've", 'with', "didn't", "what's", 'but',
    			'else', 'herself', 'than', "here's", 'he', 'me', "they're",
    			'myself', 'these', "hasn't", 'below', 'r', 'can', 'theirs', 'my',
    			'k', "we'd", 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself',
    	     	'at', 'have', 'in', 'any', 'if', 'again', 'no', 'that', 'when',
    			'same', 'how', 'other', 'which', 'you', "shan't", 'http', 'shall',
    			'our', 'after', "let's", 'most', 'such', 'on', "he'll", 'a', 'off',
    			'i', "she'd", 'yours', "you'll", 'so', "we're", "she's", 'the',
    			"that's", 'having', 'once']

    wordcount = {}
    count= 0
    for word in text.split():
        if word.lower() not in stopword:
            count += 1
    return count



f = open('/home/tengmo/workwithcrawler/2000file/sub_testcrawl[670].arc', 'r')
text = ''
cnt = 0
for line in f:
    cnt +=1
    if(cnt>7):
        text += line
html_content = text
#########################################################

soup = BeautifulSoup(html_content, 'lxml')
count = wordcount(soup.title.string)
text = soup.get_text()
new_text = ''
print(soup.title.string)
