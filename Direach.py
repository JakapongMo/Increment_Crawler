import sys
import glob
import urllib.parse

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
def File_URL(f):
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

def File_binary_domain(URL):
    Domain_name = ''
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

    return list_domain

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


cnt = 0
for name in files:
    try:
        with open(name) as f:
            #sys.stdout.write(f.read())
            cnt +=1
        #    if cnt == 3:
        #        break
            print(name ,' ',cnt)
            URL, Nb_slash, URL_length = File_URL(f)
            print('URL : ',URL,'\n','Nb of slash : ',Nb_slash,'\n','URL_length : ',URL_length)
            File_binary_domain(URL)
            list_domain = File_binary_domain(URL)
            print("binary_vector")
            for x in range(0,10):
                print(list_domain[x])

        #    for line in f:
        #        print (line)

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            print('Yo!!')
            raise
