# telelogs
telelogs is a package to send log message on your telegram if something happened on a server, e.g your training is done, update CI/CD and manymore

## How to setup the library
1. install the package
```bash
pip install https://github.com/rubythalib33/telelogs.git
```
2. search @botfather on telegram
3. click start, and type '/newbot'
4. and then you will be asked for name and username, just fill it until there's a 

Done! Congratulations on your new bot. You will find it at t.me/{your bot username}. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
YOUR_TOKEN
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

5. create a telegram group and add your bot to your telegram
6. and then type /my_id @{your bot username}
7. create telelogs.env on your project and add variable TOKEN={YOUR_TOKEN}
8. your telelogs function is ready to use

## functions
```python
#run this first before running the other function (it's just needed to be run onetime in one project you don't have to do it again forever)
retrieve_chat_id() #to retrieve chat id
print(send_massage(text:str)) #to send the message
```