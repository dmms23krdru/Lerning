#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
import os, datetime

myfile = 'base.db' # Имя файла базы данных
UsersFile = 'user.db' # Имя файла базы данных пользователей
donorfile = 'donors.txt' #  Имя файла со списком доноров

"""
if os.path.isfile(myfile):
    os.remove(myfile) # Если нужно кажды раз новый файл
    print ("delete file")
"""
dbUsers = SqliteDatabase(UsersFile)
db = SqliteDatabase(myfile)



class BaseModel(Model):
    class Meta:
        database = db

class Podpis(BaseModel):
    owner = CharField()
    pk = CharField(unique=False)
    username = CharField()
    full_name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    is_private = BooleanField()
    profile_pic_url = CharField()
    profile_pic_id = CharField(null=True)
    is_verified = BooleanField()
    has_anonymous_profile_picture = BooleanField()
    latest_reel_media = CharField(null=True)

class UsersBase(BaseModel):
    pk = CharField(unique=True)
    username = CharField()
    full_name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    is_private = BooleanField()
    profile_pic_url = CharField()
    is_verified = BooleanField()
    has_anonymous_profile_picture = BooleanField()
    media_count = CharField()
    geo_media_count = CharField(null=True)
    follower_count = CharField()
    following_count = CharField()
    following_tag_count = CharField()
    biography =  CharField()
    external_url = CharField(null=True)
    external_lynx_url = CharField(null=True)
    has_biography_translation = BooleanField(null=True)
    total_igtv_videos = CharField()
    usertags_count = CharField()
    has_chaining = BooleanField()
    hd_profile_pic_versions = CharField(null=True)
    hd_profile_pic_url_info = CharField(null=True)
    mutual_followers_count = CharField()
    direct_messaging = CharField(null=True)
    fb_page_call_to_action_id = CharField(null=True)
    address_street = CharField(null=True)
    business_contact_method = CharField(null=True)
    category = CharField(null=True)
    city_id = CharField(null=True)
    city_name = CharField(null=True)
    contact_phone_number = CharField(null=True)
    is_call_to_action_enabled = BooleanField(null=True)
    latitude = CharField(null=True)
    longitude = CharField(null=True)
    public_email = CharField(null=True)
    public_phone_country_code = CharField(null=True)
    public_phone_number = CharField(null=True)
    zip1 = CharField(null=True)
    instagram_location_id = CharField(null=True)
    is_business = BooleanField()
    account_type = CharField()
    can_hide_category = BooleanField(null=True)
    can_hide_public_contacts = BooleanField(null=True)
    should_show_category = BooleanField(null=True)
    should_show_public_contacts = BooleanField(null=True)

class UsersData(Model):
    pk = CharField(unique=True)
    username = CharField()
    full_name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    is_private = BooleanField()
    profile_pic_url = CharField()
    is_verified = BooleanField()
    has_anonymous_profile_picture = BooleanField()
    media_count = CharField()
    geo_media_count = CharField(null=True)
    follower_count = CharField()
    following_count = CharField()
    following_tag_count = CharField()
    biography =  CharField(null=True)
    external_url = CharField(null=True)
    external_lynx_url = CharField(null=True)
    has_biography_translation = BooleanField(null=True)
    total_igtv_videos = CharField(null=True)
    usertags_count = CharField()
    has_chaining = BooleanField()
    hd_profile_pic_versions = CharField(null=True)
    hd_profile_pic_url_info = CharField(null=True)
    mutual_followers_count = CharField(default='0', null=True)
    direct_messaging = CharField(null=True)
    fb_page_call_to_action_id = CharField(null=True)
    address_street = CharField(null=True)
    business_contact_method = CharField(null=True)
    category = CharField(null=True)
    city_id = CharField(null=True)
    city_name = CharField(null=True)
    contact_phone_number = CharField(null=True)
    is_call_to_action_enabled = BooleanField(null=True)
    latitude = CharField(null=True)
    longitude = CharField(null=True)
    public_email = CharField(null=True)
    public_phone_country_code = CharField(null=True)
    public_phone_number = CharField(null=True)
    zip1 = CharField(null=True)
    instagram_location_id = CharField(null=True)
    is_business = BooleanField()
    account_type = CharField()
    can_hide_category = BooleanField(null=True)
    can_hide_public_contacts = BooleanField(null=True)
    should_show_category = BooleanField(null=True)
    should_show_public_contacts = BooleanField(null=True)

    class Meta:
        database = dbUsers


UsersBase.create_table()
Podpis.create_table()
UsersData.create_table()
