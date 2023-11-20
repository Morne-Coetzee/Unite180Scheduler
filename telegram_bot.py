import configparser
import telegram

def read_config():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        bot_token = config.get('Bot', 'token')
        group_chat_id = config.get('ChatIds', 'GroupChat')
        return bot_token, group_chat_id
    except Exception as e:
        print(f"Error reading configuration: {e}")
        return None, None

async def send_telegram_message_group(message):
    try:
        print("Initializing Bot Instance")
        bot_token, group_chat_id = read_config()
        
        if bot_token and group_chat_id:
            bot = telegram.Bot(token=bot_token)
            chat_id = group_chat_id
            print("Sending Message")
            await bot.send_message(chat_id=chat_id, text=message)
        else:
            print("Invalid bot token or group chat ID.")
    except telegram.error.BadRequest as e:
        print("ERROR: {}".format(e))
