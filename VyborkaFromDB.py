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

def AddInfoUser(userName):
    api.searchUsername(userName)
    user_info = api.LastJson.get('user')
    add_UsersData(user_info)
    SleepDefault()


# alenagulchenko  223983235
count = 0
#for person in UsersData.select(): #Выбор всех записей
for person in UsersData.select().where(UsersData.is_business.contains(True)): #выборка бизнес акаунтов

    print (str(count)+ ". " + person.username + " \t \t \t \t \t" + person.full_name + " Business-" + str(person.is_business) + " " + person.city_name)
    count += 1

#for person in Person.select().where((Person.birthday < d1940) | (Person.birthday > d1960)):
#for person in Person.select().where((Person.birthday > d1940) & (Person.birthday < d1960)):	