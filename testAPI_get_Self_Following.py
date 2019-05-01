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

def AddInfoUser(userID):
    api.searchUsername(userID)
    user_info = api.LastJson.get('user')
    print (user_info)
    if UsersData.select().where(UsersData.username.contains(userID)):
    	print ('В базе присутствует!!! ', userID)
    else:
        add_UsersData (user_info)
        SleepDefault()


api.getTotalSelfFollowings()
spisok = api.LastJson.get('users')
#print (spisok)
for i in range(len(spisok)):
    userID = spisok[i]['pk']
    userName = spisok[i]['username']
    userFullName = spisok[i]['full_name']
    print (userName + '\t' + userFullName)
    print ('-' *100)
    AddInfoUser(userName)
