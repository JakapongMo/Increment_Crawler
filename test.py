import sys
#print(sys.version+'\n')

file_path = '/home/tengmo/workwithcrawler/testcrawl.arc'

def find_date(path):
    f = open(path)
    date = ''
    for line in f:
        #print (line)
        for nb in range(17,25):
            date += line[nb]
        return (date)
        break
    f.close()

def find_URL(line):
    URL = ''
    for nb in range(0,len(line)-41):
        URL += line[nb]
    print ("URL : ",URL)

#####################-main-############################

date = find_date(file_path)
print (date+'\n')

cnt = 1
f = open(file_path)
for line in f:
    if len(line) > 7:
        if str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
            print ("block",cnt)
            find_URL(line)
            cnt += 1
    print (line)
