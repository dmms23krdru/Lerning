import json
import os
import time
from InstagramAPI import InstagramAPI

##### CONFIGURATION TO USE #####
login = "login"
password = "password"
message = "Type your message here"
##### CONFIGURATION TO USE #####

api = InstagramAPI(login, password)

if (api.login()):

    user_id = api.username_id

    print("Checking if you have new followers... Please, wait.")

    #getting total followers function
    def getTotalFollowers(api, user_id):
        """
        Returns the list of followers of the user.
        It should be equivalent of calling api.getTotalFollowers from InstagramAPI
        """
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

    while True:
        followers = getTotalFollowers(api, user_id)

        # verifying if had the list of followers created
        if(os.path.isfile('./direct_message.json')):
            with open('./direct_message.json') as json_file:  
                data = json.load(json_file)
                hasNewUser = False
                for newUser in followers: # for each user founded, we verify if exists in the list of followers
                    userReceivedMessage = False
                    for user in data:
                        if(newUser['pk'] == user['pk']): # if exists, we set the variable to True
                            userReceivedMessage = True
                    if(userReceivedMessage == False): # if not exists, the variable will be False and we sent the message and save in the list of followers
                        print("New follower founded: " + str(newUser['username']) + ". Sendind message!")
                        api.direct_message(message, newUser['pk'])
                        data.append(newUser)
                        with open('./direct_message.json', 'w') as outfile:  
                            json.dump(data, outfile, indent=4)
                        hasNewUser = True
                if(hasNewUser == False):
                    print("Theres no new followers.")
        else:
            print("How its the first time that you run the script, we'd created a backup of your actual followers.")
            with open('./direct_message.json', 'w') as outfile:  
                json.dump(followers, outfile, indent=4)

        time.sleep(10)

else:
    print("Can't login!")