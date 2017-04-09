import json
import sys
import glob
import urllib.parse
from bs4 import BeautifulSoup

path = '/home/tengmo/workwithcrawler/2000file/*.arc'
#path = '/home/tengmo/workwithcrawler/store/*.arc'

files = glob.glob(path)

####################-subdef-#######################
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return True

            index += 1

    return False

####################-maindef-#####################
def Find_URL(f):
    URL = ''
    Nb_slash = 0
    before = ''
    for line in f:
        for char in line:
            if char == '/':
                Nb_slash +=1
            if char  == ' ':
                if before == '/':
                    Nb_slash -=1
                break
            URL += char
            before = char
        break

    URL = urllib.parse.unquote(URL)
    yield URL
    yield Nb_slash - 2
    yield len(URL)- 7 - Nb_slash +1

def Find_binary_domain(URL):
    Domain_name = ''
    ans = ''
    for char in URL[7:]:
        if(char == '/'):
            break
        Domain_name += char
    #print(Domain_name)

    list_string = ['.com', '.edu', '.gov', '.org', '.net', '.mil', '.co.th', '.in.th', '.ac.th']
    list_domain = [0,0,0,0,0,0,0,0,0,0]
    for x in range(0,9):
        if(find_str(Domain_name, list_string[x])):
            list_domain[x] += 1
    count = 0
    for x in range(0,9):
        if(list_domain[x] == 0):
            count +=1
    if count == 9:
        list_domain[9] +=1

    #print("binary_vector")
    #for x in range(0,10):
    #    print(list_domain[x])
    for x in range(0,10):
        ans += str(list_domain[x])

    return ans

#    com = 0
#    edu = 0
#    gov = 0
#    org = 0
#    net = 0
#    mil = 0
#    co_th = 0
#    in_th = 0
#    ac_th = 0
#    other = 0

def Find_Nb_link_pic_table(f):
    text = ''
    cnt = 0
    for line in f:
        cnt +=1
        if(cnt>7):
            text += line
    html_content = text

    soup = BeautifulSoup(html_content, 'lxml')
    soup.find_all('a')

    newtitle = ''
    title = str(soup.title)
    for x in range(0, len(title)):
        if (x>6 and x < len(title)-8):
            newtitle += title[x]
    print(newtitle)
    #print(soup.title.string)
    list_link = (soup.find_all('a'))
    list_table = (soup.find_all('table'))
    list_picture = (soup.find_all('img'))
    #print ('Nb of link: ',len(list_link))
    #print('Nb of table',len(list_table))
    #print('Nb of picture',len(list_picture))

    yield newtitle
    yield len(list_link)
    yield len(list_table)
    yield len(list_picture)

with open('/home/tengmo/workwithcrawler/json/2000_data.txt', 'w') as outfile:

    cnt = 0
    for name in files:
        try:
            with open(name) as f:
                #sys.stdout.write(f.read())
                cnt +=1
            #    if cnt == 3:
            #        break
                data = {}
                print(name ,' ',cnt)
                URL, Nb_slash, URL_length = Find_URL(f)
                print('URL : ',URL,'\n','Nb of slash : ',Nb_slash,'\n','URL_length : ',URL_length)
                Find_binary_domain(URL)
                data[URL] =[]
                binary = Find_binary_domain(URL)
                print("binary_vector")
                print(binary)
                title , link , table, picture = Find_Nb_link_pic_table(f)
                print ('Nb of link: ', link)
                print('Nb of table', table)
                print('Nb of picture',picture)


                data[URL].append({
                    'URL' : URL ,
                    'Nb of slash' : Nb_slash,
                    'URL_length' : URL_length,
                    'title' : title,
                    'binary_vector' : binary,
                    'nb of link' : link,
                    'nb of picture' : picture,
                    'nb of table' : table
                })
                json.dump(data, outfile, indent = 4)

        except IOError as exc:
            if exc.errno != errno.EISDIR:
                print('Yo!!')
                raise
