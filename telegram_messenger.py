import telegram

config = {
"the_username_of_your_bot" : 
    {
    "bot_name" : "############ Your Bot's Name #############",
    "bot_username" : "############  the_username_of_your_bot  ################",
    "bot_api_token" : '############# YOUR API TOKEN GOES HERE ##################',
    "group_chat_id" : -0000000 #Your Group Chat ID as an int.
    }
}

def bot_send(msg, bot_id, broadcast):
    """
    Send a message to a telegram user or group specified on chat_id
    chat_id must be a number!

    bot_id == bot_username
    """

    if broadcast == True:

        bot = telegram.Bot(token=config[bot_id]["bot_api_token"])
        bot.sendMessage(chat_id=config[bot_id]["group_chat_id"], text=msg)
    else:
        print(msg)

    return None