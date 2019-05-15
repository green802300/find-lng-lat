# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:30:24 2019

@author: RMS
"""

import pandas as pd
import requests
import re

data = pd.read_csv(r'C:\Users\RMS\Desktop\geocode\temp.csv')
rawinfo=data['raw_address'][:].values
simple=data['simple_address'][:].values
lng=data['longitude'][:].values
lat=data['latitude'][:].values

header={
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'content-length': '37',
'content-type': 'application/x-www-form-urlencoded',
'cookie': '_ga=GA1.2.1863798866.1557712087; _gid=GA1.2.1185045703.1557712087; PHPSESSID=ppc65va9intht2hjbptqpdh1o4',
'origin': 'https://www.latlong.net',
'Referer':'https://www.latlong.net/convert-address-to-lat-long.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'
}

for i in range(len(lng)):
    if lng[i]=='None':
        data = {'c1': simple[i],'action':'gpcm','cp':''}
        r = requests.post('https://www.latlong.net/_spm4.php', data=data,headers=header)
        if len(r.text)!=0 and len(re.split(',',r.text))==2:
            [lat[i],lng[i]]=re.split(',',r.text)
            print('Changed',i)
        else:
            print('Not Changed',i)

for i in range(len(lng)):
    if lng[i]=='None':
        n=re.split(',',rawinfo[i])
        m=n[-2]+','+n[-1]
        data = {'c1': m,'action':'gpcm','cp':''}
        r = requests.post('https://www.latlong.net/_spm4.php', data=data,headers=header)
        if len(r.text)!=0 and len(re.split(',',r.text))==2:
            [lat[i],lng[i]]=re.split(',',r.text)
            print('Changed',i)
        else:
            print('Not Changed',i)

count=0
for i in range(len(lng)):
    if lng[i]=='None' or lng[i]=='None1':
        count+=1
count

name=['raw_address']
test=pd.DataFrame(columns=name,data=rawinfo)
test['simple_address']=simple
test['longitude']=lng
test['latitude']=lat
test.to_csv(r'C:\Users\RMS\Desktop\geocode\complete.csv',encoding='gbk')
