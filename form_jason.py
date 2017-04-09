import sys
import json


data = {}
data['web_page'] =[]
data['web_page'].append({
    'URL' : ,
    'Nb of slash' : ,
    'URL_length' : ,
    'com' : ,
    'edu' : ,
    'gov' : ,
    'org' : ,
    'net' : ,
    'mil' : ,
    'co_th' : ,
    'in_th' : ,
    'ac_th' : ,
    'other' :


})

with open('/home/tengmo/workwithcrawler/json/data.txt', 'w') as outfile:
    json.dump(data, outfile, indent = 4)
