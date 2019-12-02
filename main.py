import configparser
import epsimplelib
import time
import datetime
import telepot
from telepot.loop import MessageLoop
import textwrap

config = configparser.RawConfigParser()
config.read('config.ini')
telegram_bot_config = config.get('telegram', 'bot_id')


# eInk
EPD_WIDTH = 176
EPD_HEIGHT = 264


def toPercentHeight(num):
    return num * .01 * EPD_HEIGHT


def toPercentWidth(num):
    return num * .01 * EPD_WIDTH


def display(title, msgs):
    eps = epsimplelib.EPScreen('landscape')  # eps = e-Ink Paper Screen
    # print(len(msgs))
    if title:
        eps.set_title('From ' + title + ':')
    # eps.add_text_middle(toPercentWidth(25), "<3 <3 <3")
    if len(msgs) == 1:
        width = 20
        # print(len(msgs[0]))
        if len(msgs[0]) > width:
            positionX = 25
            myNewText = textwrap.wrap(msgs[0], width=width)
            for i in range(len(myNewText)):
                eps.add_text_middle(toPercentWidth(positionX), myNewText[i])
                positionX = positionX + 20
        else:
            eps.add_text_middle(toPercentWidth(45), msgs[0])
    elif len(msgs) == 2:
        eps.add_text_middle(toPercentWidth(30), msgs[0])
        eps.add_text_middle(toPercentWidth(50), msgs[1])
    # eps.add_text_middle(toPercentWidth(60), "girls very much!!!")
    # eps.add_text_middle(toPercentWidth(80), "<3 <3 <3")

    # TODO: Figure out how the hell to make a heart from lines
    # eps.add_line((40, 40, 41, 40))
    # eps.add_line((100, 100, 165, 100))
    eps.update_screen()


# hello()
# hello()  # Physical screen not refreshed


# Telegram Bot


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    # print(msg['from']['username'])

    # print('Received: %s' % command)

    if command.startswith('/hi'):
        telegram_bot.sendMessage(chat_id, str(
            "Hi, " + msg['from']['first_name'] + '!'))
        print('msg: "' + msg['text'] + '"\
             from: ' + msg['from']['username'])
    elif command == '/time':
        now = datetime.datetime.now()
        telegram_bot.sendMessage(chat_id, str(
            now.hour)+str(":")+str(now.minute))
    # elif command == '/logo':
    #     telegram_bot.sendPhoto (chat_id, photo = "https://i.pinimg.com/avatars/circuitdigest_1464122100_280.jpg")
    # elif command == '/file':
    #     telegram_bot.sendDocument(chat_id, document=open('/home/pi/Aisha.py'))
    # elif command == '/audio':
    #     telegram_bot.sendAudio(chat_id, audio=open('/home/pi/test.mp3'))
    elif command.startswith('/display '):
        display(msg['from']['first_name'],
                [msg['text'].replace("/display ", "")])
        telegram_bot.sendMessage(chat_id, str(
            'Your message has been displayed.'))
        print('display: "' + msg['text'].replace("/display ", "") + '"\
             from: ' + msg['from']['username'])
    elif command == '/headinghome':
        now = datetime.datetime.now()
        display("", [msg['from']['first_name'] + ' is heading home', 'at ' + now.strftime("%m/%d/%Y, %H:%M:%S")])
        telegram_bot.sendMessage(chat_id, str(
            'Your message has been displayed.'))
        print('display: "' + msg['text'].replace("/display ", "") + '"\
             from: ' + msg['from']['username'])

telegram_bot = telepot.Bot(telegram_bot_config)
print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')

while 1:
    time.sleep(10)
