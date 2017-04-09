import sys
from bs4 import BeautifulSoup

def initial():
    f = open('/home/tengmo/workwithcrawler/2000file/sub_testcrawl[1791].arc', 'r')
    text = ''
    cnt = 0
    for line in f:
        cnt +=1
        if(cnt>7):
            text += line
    html_content = text

    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.get_text()
    new_text = ''
    for char in text:
        #if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >=97 and ord(char) <=122) or ord(char)==40 or ord(char) ==10 or ord(char)==32) or (ord(char) >= 48 and ord(char) <= 57):
            new_text += char

    return new_text

def check_charset_thai(char):
    if(char >= 3584 and char <= 3711):
        return True
    else:
        return False

new_text = initial()
new_text = "".join(new_text.split())
print (new_text)
print (ord(new_text[0]))

count = 0
for x in range(0,5):
    if (check_charset_thai(ord(new_text[x]))):
        count += 1
        #print ("KUY TO")

if count >=3:
    print ("KUY TO")
output = ''
for x in range(0,len(new_text)):
    if (check_charset_thai(ord(new_text[x]))):
        output += new_text[x]
print (output)
with open('/home/tengmo/workwithcrawler/output_thai/output.txt' , 'a') as out:
    out.write(output)
