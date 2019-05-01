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

unfolowfile='unfolow.txt'

api = InstagramAPI(cred.login, cred.passw)
api.login()

# Открываем фаил с с перечнем пользователей для отписки
handle = open(unfolowfile, 'r')
Ldonors = []
with handle as f:
    Ldonors = f.read().splitlines()
#Заполнили базу именами доноров
for i in range(len(Ldonors)):
    donor_name = Ldonors[i].strip()
    if str(donor_name): # Отсечение пустых строк
        print ('_' * 100)
        print (u'Работем с пользователем ' + donor_name)
        api.searchUsername(donor_name)
        spisok = api.LastJson.get('user')
        userId = spisok['pk']
        #print (userId)
        LimitUnFollow()
        api.unfollow(userId)
        print ('Отписан от ' + donor_name)

