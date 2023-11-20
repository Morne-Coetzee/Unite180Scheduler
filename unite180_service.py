# Imports
import time
import schedule
import datetime
import logging
import asyncio
import configparser
from math import ceil
from decouple import *
from cryptography.fernet import Fernet

# Extra Imports
from telegram_bot import send_telegram_message_group

# Version - To be updated with each release
current_version = 'Version : 1.00'

# Get current date
time_stamp = datetime.datetime.now()

# Create a custom logger
logger = logging.getLogger('root')
logger.setLevel(logging.INFO)

####### Setup #######

config = configparser.ConfigParser()

def read_config():
    try:
        config.read('config.ini')
        dbsettings = {}
        dbsettings["dbhost"] = config.get('Database', 'dbhost')
        dbsettings["dbport"] = config.getint('Database', 'dbport')
        dbsettings["dbuser"] = config.get('Database', 'dbuser')
        dbsettings["dbpass"] = config.get('Database', 'dbpass')
        dbsettings["dbname"] = config.get('Database', 'dbname')
        return dbsettings
    except Exception as e:
        logger.error(e)

# Default Log Levels
StreamHandler_Level = "20"
FileHandler_Level = "20"

# Get log levels
def get_loglevel():
    try:
        config.read('config.ini')

        log_level = {}
        log_level["StreamHandler_Level"] = config.get('LogLevels', 'StreamHandler_Level')
        log_level["FileHandler_Level"] = config.get('LogLevels', 'FileHandler_Level')
        return log_level
    except Exception as e:
        logger.error(e)

# Get week number of month
def get_week_no_of_month(dt):
    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()
    return int(ceil(adjusted_dom/7.0))

# Create handlers
log_level = get_loglevel()
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('unite180_sheduler.log')
if log_level["StreamHandler_Level"] == 'logging.INFO':
    StreamHandler_Level = 20
if log_level["StreamHandler_Level"] == 'logging.WARNING':
    StreamHandler_Level = 30
if log_level["StreamHandler_Level"] == 'logging.DEBUG':
    StreamHandler_Level = 10
if log_level["StreamHandler_Level"] == 'logging.ERROR':
    StreamHandler_Level = 40
if log_level["FileHandler_Level"] == 'logging.INFO':
    FileHandler_Level = 20
if log_level["FileHandler_Level"] == 'logging.WARNING':
    FileHandler_Level = 30
if log_level["FileHandler_Level"] == 'logging.DEBUG':
    FileHandler_Level = 10
if log_level["FileHandler_Level"] == 'logging.ERROR':
    FileHandler_Level = 40

# Set log level
c_handler.setLevel(int(StreamHandler_Level))
f_handler.setLevel(int(FileHandler_Level))

# Create formatters and add it to handlers
c_format = logging.Formatter('%(asctime)s - %(funcName)s[%(lineno)d] - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(funcName)s[%(lineno)d] - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

####### Jobs #######

def send_birtday_discord():
    try:
        logger.info('Started: send_birtday_discord')
        message = config.get('Messages', 'Birthday')
        message = message.encode('utf-8').decode('unicode-escape')
        if message:
            asyncio.run(send_telegram_message_group(message))
        else:
            logger.error("No message for birthdays")
        logger.info('Finished: send_birtday_discord')
    except Exception as e:
        logger.error(e)

####### Schedules #######

schedule.every().day.at("20:20").do(send_birtday_discord)

# Log messages
logger.info(current_version)
logger.info("Ready For Action")

# Scheduler loop
while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
