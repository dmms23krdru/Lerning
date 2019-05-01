#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import os
from InstagramAPI import InstagramAPI
from datetime import datetime, date
import cred
from oper import *
from model import *
import peewee

db = SqliteDatabase(UsersFile)
db.connect()

api = InstagramAPI(cred.login, cred.passw)
api.login()
user_id = api.username_id

def AddInfoUser(userName):
    api.searchUsername(userName)
    user_info = api.LastJson.get('user')
    add_UsersData(user_info)
    SleepDefault()

"""
    #print (user_info)
    if UsersData.select().where(UsersData.username.contains(userName)):
        print ('В базе присутствует!!! ', userName)
    else:
        add_UsersData (user_info)
        SleepDefault()
"""



# alenagulchenko  223983235
count = 0

#spisok = getTotalFollowings(api, '223983235') # Подписки
spisok = getTotalFollowers(api, '223983235') # Получаем данные о Подписчиках
#spisok = api.LastJson.get('users')
##print (spisok)
for i in range(len(spisok)):    
    userID = spisok[i]['pk']
    userName = spisok[i]['username']
    userFullName = spisok[i]['full_name']
    print ('-' *100)
    print (count)
    print (userName + '\t' + userFullName)
    count += 1
    if UsersData.select().where(UsersData.pk.contains(userID)):
        print ('В базе присутствует!!! ', userName)
        pass  # Возможно стоит хотя бы записать исключение в журнал.

    else:
        AddInfoUser(userName)



"""
followers_donor = getTotalFollowers(api, person.pk) # Получаем данные о фоловерах
for i in range(len(followers_donor)):
    follower_l = followers_donor[i].get('pk')
    #print (follower_l)
    if CheckNewUser_ID(follower_l, ids):
        #print ('New user')
        ids.add(str(follower_l))
        add_podpis(donor_name, followers_donor[i]) # добавляем подписчика
        texts =str (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' Add new user: https://www.instagram.com/' + str(followers_donor[i].get('username'))+ '\n'
        wrfile('work.log',texts) #запись в лог файл
        fname = datetime.datetime.now().strftime('%d_%m_%Y') + '_Followers.log'
        texts = str(followers_donor[i].get('username'))+ '\n'
        wrfile(fname, texts) #запись для анализа
"""