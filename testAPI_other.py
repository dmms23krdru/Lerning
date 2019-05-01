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

db = SqliteDatabase(myfile)
db.connect()


api = InstagramAPI(cred.login, cred.passw)
api.login()
# user_id = '1461295173'
user_id = api.username_id
donor_name = 'elenafotodiva'
#donor_info = (getUserInfo(api, donor_name))
#add_UsersBase (donor_info)

# Получение перечня своих публикаций 
#api.getSelfUserFeed() 
#MediaList = api.LastJson 
#print (MediaList)
#------------------

#api.getPopularFeed() #Лента популярных фото????
api.getSelfUserFeed() #Собственая лента своих фото
api.getMediaLikers('1569618519111465714_146199240')
PopFeed = api.LastJson

#len(PopFeed['items']) #Количесво секций taken_at

print (PopFeed)
print ('-' *100)

for i in range(len(PopFeed['users'])):
    Content = PopFeed['users'][i]
    print (Content)
    print ('-' *100)


#for i in range(len(PopFeed['items'])):
 #   Content = PopFeed['items'][i]
 #  print (Content)
 #   print ('-' *100)






#for i in range(5):
##    #Content = PopFeed['items'][0]['image_versions2']['candidates'][0]
#    Content = PopFeed['items'][i]
#    Content1 = PopFeed['items'][i]['image_versions2']['candidates'][0]['url']
#    print (Content1)
#    print ('-' *100)
    #print (len(Content))




#len(PopFeed['items']) #Количесво секций taken_at

"""
for i in range(len(Content)):
	Content = PopFeed['items'][0]['image_versions2']['candidates'][i]
	print (Content['url'])
#print (Content[0]['candidates'])


#api.getUserFeed('223983235') #Получение списка публикаций
api.getMediaLikers(2023918948977834960_223983235)
MediaList = api.LastJson
#print (MediaList)
#print ('-' * 100)
Media = MediaList['items'][3]
MediaID = Media['id']
MediaType = Media['media_type']
MediaCode = Media['code']

print (Media)
print ('-' * 100)
print (MediaID)
print ('-' * 100)
print (MediaType)
print ('-' * 100)
print (MediaCode)
print ('-' * 100)

#api.like(MediaID) #Лайк контента
"""
