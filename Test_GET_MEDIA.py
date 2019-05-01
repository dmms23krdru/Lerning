#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *
#from oper import *
from InstagramAPI import InstagramAPI
import cred, peewee

ig = InstagramAPI(cred.login, cred.passw)
ig.login()


# get Self user feed 
ig.getSelfUserFeed()

# get response json and assignment value to MediaList Variable
# dict type data 
MediaList = ig.LastJson 

# get first media for example delete media
Media = MediaList['items'][0]

# get media ID 

MediaID = Media['id']
MediaType = Media['media_type']
print (MediaID, MediaType)