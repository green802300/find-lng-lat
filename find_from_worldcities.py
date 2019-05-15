# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:09:06 2019

@author: RMS
"""

import pandas as pd
import re

data = pd.read_excel(r'C:\Users\RMS\Desktop\geocode\address.xlsx',header = None)
df=pd.read_excel(r'C:\Users\RMS\Desktop\geocode\worldcities.xlsx')
cities=df['city_ascii'][:].values
cities2=df['city'][:].values
cou=df['country'][:].values
longitude=df['lng'][:].values
latitude=df['lat'][:].values
rawinfo=data[0][:].values

ans=[]
countries=[]
lng=[]
lat=[]
for item in rawinfo:
    raw=re.split(",",item)
    res=re.split(" |,",item)
    if 'USA' in raw[-1][0:-1]:
        c='USA'
    else:
        c=raw[-1][0:-1]
    countries.append(c)    
    flag0=0
    for j in range(len(res)):
        for i in range(len(cities)):
            if res[j] == cities[i] and cou[i] == c:
                lng.append(longitude[i])
                lat.append(latitude[i])
                ans.append(cities[i]+','+c)
                flag0=1
                break    
        if i==len(cities)-1 and j==len(res)-1:        
            lng.append('None')
            lat.append('None')
            ans.append(raw[0]+','+c)
        if flag0==1:
            break

flag1=0
for k in range(len(ans)):
    if lng[k]=='None':
        raw=re.split(",",rawinfo[k])
        if 'USA' in raw[-1][0:-1]:
            c='USA'
        else:
            c=raw[-1][0:-1]
        for j in range(len(raw)):
            for i in range(len(cities)):
                if cities[i] in rawinfo[k]  and cou[i] == c:
                    lng[k]=longitude[i]
                    lat[k]=latitude[i]
                    ans[k]=cities[i]+','+c
                    flag1=1
                    break    
            if flag1==1:
                break

flag2=0
for k in range(len(ans)):
    if lng[k]=='None':
        raw=re.split(",",rawinfo[k])
        if 'USA' in raw[-1][0:-1]:
            c='USA'
        else:
            c=raw[-1][0:-1]
        for j in range(len(raw)):
            for i in range(len(cities)):
                if cities[i] in rawinfo[k]  and cou[i] == 'Hong Kong':
                    lng[k]=longitude[i]
                    lat[k]=latitude[i]
                    ans[k]=cities[i]+','+c
                    flag2=1
                    break    
            if flag2==1:
                break


flag3=0
for k in range(len(ans)):
    if lng[k]=='None':
        raw=re.split(",",rawinfo[k])
        res=re.split(" |,",item)
        if 'USA' in raw[-1][0:-1]:
            c='USA'
        else:
            c=raw[-1][0:-1]
        for j in range(len(res)):
            for i in range(len(cities)):
                if (cities[i] == res[j] or cities2[i]==res[j]) and cou[i] == c:
                    lng[k]=longitude[i]
                    lat[k]=latitude[i]
                    ans[k]=cities[i]+','+c
                    flag3=1
                    break    
            if flag3==1:
                break


count=0
for _ in lng:
    if _ == 'None':
        count+=1
count

raw=re.split(",",rawinfo[10])
for _ in raw:
    print(_)
raw[4]
raw[4] in cities

name=[' raw_address']
test=pd.DataFrame(columns=name,data=rawinfo)

test['simple_address']=ans
test['longitude']=lng
test['latitude']=lat


test.to_csv(r'C:\Users\RMS\Desktop\geocode\temp.csv',encoding='gbk')

