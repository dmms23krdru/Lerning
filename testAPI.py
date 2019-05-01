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

if __name__ == "__main__":
    api = InstagramAPI(cred.login, cred.passw)
    api.login()
    # user_id = '1461295173'
#    user_id = api.username_id
    donor_name = 'alenastepanenko'
 #   donor_info = (getUserInfo(api, donor_name))
#    add_UsersBase (donor_info)
    for person in UsersBase.select().where(UsersBase.username == donor_name):
        print (person.username, person.pk)
        followers_donor = getTotalFollowers(api, person.pk)
        for i in range(len(followers_donor)):
            follower_l = followers_donor[i]
            add_podpis(donor_name, follower_l)


"""
for person in Podpischiki.select().where(Podpischiki.pk == '276049797'):
    print (person.owner, person.username, person.pk)
"""

