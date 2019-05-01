#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import * 
from oper import *
from InstagramAPI import InstagramAPI
import cred, peewee, os, datetime

db = SqliteDatabase(myfile)
db.connect()

ids = LoadUsersBase() #Загрузка базы подписчиков в множество ids
#print (ids)

api = InstagramAPI(cred.login, cred.passw)
api.login()

# Открываем фаил с донормаи
handle = open(donorfile, 'r')
Ldonors = []
with handle as f:
    Ldonors = f.read().splitlines()
#Заполнили базу именами доноров
for i in range(len(Ldonors)):
    donor_name = Ldonors[i].strip()
    if str(donor_name): # Отсечение пустых строк
        print ('_' * 100)
        print (u'Работем с пользователем ' + donor_name)
        if CheckNewUserName(donor_name):
            #print ('https://www.instagram.com/' + username + '/'), username
            #print ('New? ' + str(CheckNewUser(user_id)))
            donor_info = (getUserInfo(api, donor_name))
            add_UsersBase (donor_info) # Добавление  записи
        else:
            print (u'Имя в базе уже есть!!!')
#-------------------------------------------------

# Сбор фолооверов по донорам
for i in range(len(Ldonors)):
    donor_name = Ldonors[i].strip()
    if str(donor_name): # Отсечение пустых строк
        print ('-'*100)
        print ('Работаем с ', donor_name)
        for person in UsersBase.select().where(UsersBase.username == donor_name):
            donor_info = (getUserInfo(api, donor_name)) #Получили инфо по донору

            if int(donor_info.get('follower_count')) > int(person.follower_count): # Если у донора больше подписч чем в базе 
                print ('Есть новые пользователи')
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
                        #пока не получены данные повсем закоментить
                        ##if CheckNewUserName(followers_donor[i].get('username')):
                            ##user_info = (getUserInfo(api, followers_donor[i].get('username')))
                            ##add_UsersBase (user_info) # Добавление  записи
                        ##else:
                            ##print (u'Имя в базе уже есть!!!')
                        #-----------------------------
                    else:
                        null_variable = None
                        #print ('Уже есть в базе')
                
                person.follower_count = donor_info.get('follower_count') # Обновляем счетчик в базе

            elif int(donor_info.get('follower_count')) == int(person.follower_count): # Если у донора не изменений :
                print ('Новых нет')
                null_variable = None

            else:
                print ('Кто-то отписался')
                person.follower_count = donor_info.get('follower_count') # Обновляем счетчик в базе
                null_variable = None

            person.save() # обновим запись  в  базе

 






"""
    for person in UsersBase.select().where(UsersBase.username == donor_name):
        #print (person.username, person.pk)
        followers_donor = getTotalFollowers(api, person.pk)
        for i in range(len(followers_donor)):
            follower_l = followers_donor[i]
            add_podpis(donor_name, follower_l)




    for person in Podpischiki.select().where(Podpischiki.username == user_name):
#        print (person.owner, person.username, person.pk)
        print (person.pk)


for person in Podpischiki.select().where(Podpischiki.pk == '276049797'):
    print (person.owner, person.username, person.pk)

    """
if not db.is_closed():
    db.close() 