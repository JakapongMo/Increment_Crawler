import sys
import os
#print(sys.version+'\n')


file_path = '/home/tengmo/Desktop/Project crawler/filtercrawl-20170101054747-00000.arc'
#file_path = '/home/tengmo/workwithcrawler/testcrawl.arc'
#file_path = '/home/tengmo/workwithcrawler/filter10000.arc'
#file_path = '/home/tengmo/workwithcrawler/test.txt'
sub_file_path = '/home/tengmo/workwithcrawler/sub_testcrawl.arc'



def Find_date(path):
    f = open(path, "r")
    date = ''
    for line in f:
        #print (line)
        for nb in range(17,25):
            date += line[nb]
        return (date)
        break
    f.close()

def Find_URL(line):
    URL = ''
    for nb in range(0,len(line)-41):
        URL += line[nb]
    print ("URL : ",URL)

def Cal_Block(sub_f):
    print ("haha")
    sub_f = open(sub_file_path)
    for line in sub_f:
        print (line)

#####################-main-############################

date = Find_date(file_path)
print (date+'\n')

cnt = 0
check = 1
f = open(file_path, "r", errors='ignore')
sub_f = open('/home/tengmo/workwithcrawler/store/sub_testcrawl[1].arc', 'w+')
for line in f:
    if len(line) > 7:
        if str(line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]) == 'http://':
            cnt += 1
            print ("block",cnt)
            #Find_URL(line)
    print (line)
    if cnt == check:
        sub_f.write(line)
    ###เช็คว่ามันควรคำนวณรึยัง###
    if cnt - check == 1:
        sub_f.close
        #Cal_Block(sub_f)
        #if cnt == 2:
        #    break
        ############################os.remove(sub_file_path)
        sub_f = open('/home/tengmo/workwithcrawler/store/sub_testcrawl[%d].arc'%cnt, 'w+')
        sub_f.write(line)
        check +=1
