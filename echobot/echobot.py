import os
import time
from slackclient import SlackClient


# CPS-847-Bot Slack access token
Bot_User_OAuth_Access_Token = 'xoxb-929661055991-921047749811-zolmWoL5Yz1rG8TMAQ54ET34'
SLACK_API_TOKEN = Bot_User_OAuth_Access_Token

# Hardcoded SLACK_API_TOKEN
slack_token = SLACK_API_TOKEN
bot = SlackClient(slack_token)

def main():
    if bot.rtm_connect():
        print('Starting echo bot...')
        # read incoming message 
        while True:
            messages = bot.rtm_read()
            print(messages)
            for update in messages:
                # for debuging purposes, to make sure that we are in the for loops
                print('Update found!')
                # if user is typing and the typed message is indeed the message then we send echo
                if 'type' in update and update['type'] == 'message':
                    # for debuging purposes, to make sure the if statement is true
                    print('sending message!')
                    # send the echo
                    bot.rtm_send_message(update['channel'], update['text'])
                
                # if 'type' in update and update['type'] == 'message':
                #     # for debuging purposes, to make sure the if statement is true
                #     print('sending message!')
                #     # send the echo
                #     bot.rtm_send_message(update['thread_ts'], update['text'])
            time.sleep(1)
    else:
        print("Connection Failed")

if __name__ == '__main__':
    main()