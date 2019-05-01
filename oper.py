# -*- coding: utf-8 -*-

import peewee, time
from model import *
from random import randint

db = SqliteDatabase(myfile)

if __name__ == '__main__':
    try:
        db.connect()
        UsersBase.create_table()
        Podpis.create_table(safe=True)
    except peewee.InternalError as px:
        print(str(px))

# Загрука ИД в множество для вычесления уникальных пользователей 
def LoadUsersBase():
    print ('Load base to mem...')
    # загрузка базы в множество
    ids = set()
    for use_base in Podpis.select():
        ids.add(use_base.pk)
    print ('End loading! \n')
    return ids
#---------------------------------------------------------------

#Получение info о пользователе
def getUserInfo(api, user_name):
    api.searchUsername(user_name)
    info = api.LastJson.get('user')
    return info
#---------------------------------------------------------------

#Получение фолловеров донора
def getTotalFollowers(api, user_id): # Подписчики
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers
#---------------------------------------------------------------


#Вставка записи в базу данных UsersBase
def add_UsersBase(user_info):
    try:
        row = UsersBase(
            pk = user_info.get('pk'),
            username = user_info.get('username'),
            full_name = user_info.get('full_name'),
            is_private = user_info.get('is_private'),
            profile_pic_url = user_info.get('profile_pic_url'),
            is_verified = user_info.get('is_verified'),
            has_anonymous_profile_picture = user_info.get('has_anonymous_profile_picture'),
            media_count = user_info.get('media_count'),
            geo_media_count = user_info.get('geo_media_count'),
            follower_count = user_info.get('follower_count'),
            following_count = user_info.get('following_count'),
            following_tag_count = user_info.get('following_tag_count'),
            biography = user_info.get('biography'),
            external_url = user_info.get('external_url'),
            external_lynx_url = user_info.get('external_lynx_url'),
            has_biography_translation = user_info.get('has_biography_translation'),
            total_igtv_videos = user_info.get('total_igtv_videos'),
            usertags_count = user_info.get('usertags_count'),
            is_favorite = user_info.get('is_favorite'),
            has_chaining = user_info.get('has_chaining'),
            hd_profile_pic_versions = user_info.get('hd_profile_pic_versions'),
            hd_profile_pic_url_info = user_info.get('hd_profile_pic_url_info'),
            mutual_followers_count = user_info.get('mutual_followers_count'),
            profile_context = user_info.get('profile_context'),
            profile_context_links_with_user_ids = user_info.get('profile_context_links_with_user_ids'),
            profile_context_mutual_follow_ids = user_info.get('profile_context_mutual_follow_ids'),
            direct_messaging = user_info.get('direct_messaging'),
            fb_page_call_to_action_id = user_info.get('fb_page_call_to_action_id'),
            address_street = user_info.get('address_street'),
            business_contact_method = user_info.get('business_contact_method'),
            category = user_info.get('category'),
            city_id = user_info.get('city_id'),
            city_name = user_info.get('city_name'),
            contact_phone_number = user_info.get('contact_phone_number'),
            is_call_to_action_enabled = user_info.get('is_call_to_action_enabled'),
            latitude = user_info.get('latitude'),
            longitude = user_info.get('longitude'),
            public_email = user_info.get('public_email'),
            public_phone_country_code = user_info.get('public_phone_country_code'),
            public_phone_number = user_info.get('public_phone_number'),
            zip1 = user_info.get('zip'),
            instagram_location_id = user_info.get('instagram_location_id'),
            is_business = user_info.get('is_business'),
            account_type = user_info.get('account_type'),
            can_hide_category = user_info.get('can_hide_category'),
            can_hide_public_contacts = user_info.get('can_hide_public_contacts'),
            should_show_category = user_info.get('should_show_category'),
            should_show_public_contacts = user_info.get('should_show_public_contacts'),
        )
        row.save()
        print (u'Добавлен в базу!')
    except peewee.InternalError as px:
        print ('Пользователь не добавлен ', username)
        print(str(px))
#---------------------------------------------------------------
#Вставка записи в базу данных UsersBase
def add_UsersData(user_info):
    try:
        row = UsersData(
            pk = user_info.get('pk'),
            username = user_info.get('username'),
            full_name = user_info.get('full_name'),
            is_private = user_info.get('is_private'),
            profile_pic_url = user_info.get('profile_pic_url'),
            is_verified = user_info.get('is_verified'),
            has_anonymous_profile_picture = user_info.get('has_anonymous_profile_picture'),
            media_count = user_info.get('media_count'),
            geo_media_count = user_info.get('geo_media_count'),
            follower_count = user_info.get('follower_count'),
            following_count = user_info.get('following_count'),
            following_tag_count = user_info.get('following_tag_count'),
            biography = user_info.get('biography'),
            external_url = user_info.get('external_url'),
            external_lynx_url = user_info.get('external_lynx_url'),
            has_biography_translation = user_info.get('has_biography_translation'),
            total_igtv_videos = user_info.get('total_igtv_videos'),
            usertags_count = user_info.get('usertags_count'),
            is_favorite = user_info.get('is_favorite'),
            has_chaining = user_info.get('has_chaining'),
            hd_profile_pic_versions = user_info.get('hd_profile_pic_versions'),
            hd_profile_pic_url_info = user_info.get('hd_profile_pic_url_info'),
            mutual_followers_count = user_info.get('mutual_followers_count'),
            profile_context = user_info.get('profile_context'),
            profile_context_links_with_user_ids = user_info.get('profile_context_links_with_user_ids'),
            profile_context_mutual_follow_ids = user_info.get('profile_context_mutual_follow_ids'),
            direct_messaging = user_info.get('direct_messaging'),
            fb_page_call_to_action_id = user_info.get('fb_page_call_to_action_id'),
            address_street = user_info.get('address_street'),
            business_contact_method = user_info.get('business_contact_method'),
            category = user_info.get('category'),
            city_id = user_info.get('city_id'),
            city_name = user_info.get('city_name'),
            contact_phone_number = user_info.get('contact_phone_number'),
            is_call_to_action_enabled = user_info.get('is_call_to_action_enabled'),
            latitude = user_info.get('latitude'),
            longitude = user_info.get('longitude'),
            public_email = user_info.get('public_email'),
            public_phone_country_code = user_info.get('public_phone_country_code'),
            public_phone_number = user_info.get('public_phone_number'),
            zip1 = user_info.get('zip'),
            instagram_location_id = user_info.get('instagram_location_id'),
            is_business = user_info.get('is_business'),
            account_type = user_info.get('account_type'),
            can_hide_category = user_info.get('can_hide_category'),
            can_hide_public_contacts = user_info.get('can_hide_public_contacts'),
            should_show_category = user_info.get('should_show_category'),
            should_show_public_contacts = user_info.get('should_show_public_contacts'),
        )
        row.save()
        print (u'Добавлен в базу!')
    except peewee.InternalError as px:
        print ('Пользователь не добавлен ', username)
        print(str(px))
#---------------------------------------------------------------

#Запись в файл
def wrfile(fname,texts):
    handle = open(fname, "a", encoding='utf-8')
#    handle.write(texts+'\n')
    handle.write(texts)
    handle.close()
#---------------------------------------------------------------

#Вставка записи в базу данных Podpis
def add_podpis(donor_name, user_info):
    try:
        row = Podpis(
            owner = donor_name,
            pk = user_info.get('pk'),
            username = user_info.get('username'),
            full_name = user_info.get('full_name'),
            is_private = user_info.get('is_private'),
            profile_pic_url = user_info.get('profile_pic_url'),
            profile_pic_id = user_info.get('profile_pic_id'),
            is_verified = user_info.get('is_verified'),
            has_anonymous_profile_picture = user_info.get('has_anonymous_profile_picture'),
        )
        row.save()
        print (u'Добавлен в базу!', user_info.get('username'))
    except peewee.InternalError as px:
        print (u'Пользователь не добавлен ', user_info.get('username'))
        print(str(px))
#---------------------------------------------------------------

#Поиск вхождений по имени
def CheckNewUserName(username):
    statususer = ''
    new_user = UsersBase.select().where(UsersBase.username.contains(username))
    if  new_user:
       # Найдено вхождение пользователь существует
        statususer=False
    else:
        # не наайдено вхождений пользователь новый
        statususer=True
    return statususer
#---------------------------------------------------------------

#Поиск вхождений по user_id
def CheckNewUser_ID(pk, ids):
    user_s = set()
    user_s.add(str(pk))
    #print (user_s)
    if  user_s.issubset(ids):
        # Найдено вхождение пользователь существует
        ##print ('New followers no found!!!')
        status = False
    else:
        status = True
    user_s.clear()
    return status
#---------------------------------------------------------------

# вывод времени задержки
def printLimit(n):
    print("Sleep for seconds: " + str(n))
#---------------------------------------------------------------

#ЗадержкаДефолная
def SleepDefault():
    # sleep for random between 600 - 1200s
    n = randint(3, 11)
    printLimit(n)
    time.sleep(n)
#---------------------------------------------------------------

#ЗадержкаДефолная
def SleepR():
    # sleep for random between 600 - 1200s
    n = randint(600, 1200)
    printLimit(n)
    time.sleep(n)
#---------------------------------------------------------------

# Лайки: не более одного в течении 28 – 36 секунд (за раз – 1000, перерыв 24 часа);
def SleepLikes():
    CountLikes =+ 1
    n = randint(28, 38)
    printLimit(n)
    time.sleep(n)
#-------------------------------------------------

# Подписки: не более одной в течении 28 – 38 секунд и не более 200 в час (за сутки – 1000, перерыв 24 часа);
def LimitFollow():
    CountFollow =+ 1
    n = randint(28, 38)
    printLimit(n)
    time.sleep(n)
#-------------------------------------------------

# Подписка + Лайк: не более 2000 (1000 + 1000) в сутки с интервалом 28 – 38 секунд;
def LimitFollow_Like():
    CountFollow_Like =+ 1
    n = randint(28, 38)
    printLimit(n)
    time.sleep(n)
#-------------------------------------------------

# Отписка: интервал 12-22 секунд и не более 1000 в сутки от НЕвзаимных и 1000 от взаимных (пауза между невзаимными и взаимными 15 часов);
def LimitUnFollow():
    CountUnFollow =+ 1
    n = randint(12, 22)
    printLimit(n)
    time.sleep(n)
#-------------------------------------------------

# Лимиты Директ: интервал рассылки от 450 до 650 секунд, отправка сообщений подписчикам не более 100 в сутки, 
# сообщения НЕподписчикам 30-40 в сутки, вообще ситуация с отправкой сообщений в Direct нефоловерам - тема очень спорная
# и всегда на грани, если этим злоупотреблять, то будет печаль у аккаунта;
def LimitDireckt():
    CountDireckt =+ 1
    n = randint(450, 650)
    printLimit(n)
    time.sleep(n)
#-------------------------------------------------

#Упоминания: 5 ников в одном сообщении с задержкой 350-450 секунд;
def LimitNick():
    CountNick =+ 1
    n = randint(350, 450)
    printLimit(n)
    time.sleep(n)
#-------------------------------------------------

#Комментарии: не более 12-14 в час с задержкой от 350 до 400 сек, любое превышение лимитов может быть воспринято как спам.
def LimitComents():
    CountComents =+ 1
    n = randint(350, 400)
    printLimit(n)
    time.sleep(n)
#-------------------------------------------------

#Добавление фотографий: на новом аккаунте инстаграм нельзя добавлять сразу много новых фото, желательно не более 2-3 в день, для старых аккаунтов не более 9-12 фотографий
def LimitPhoto():
    CountPhoto =+ 1
    n = randint(350, 400)
    printLimit(n)
    time.sleep(n)
#-------------------------------------------------

#LimitOtpiski()