import epsimplelib
import time
import datetime
import telepot
from telepot.loop import MessageLoop
import textwrap

from PIL import Image

from math import cos, sin

# eInk
EPD_WIDTH = epsimplelib.DEVICE_WIDTH
EPD_HEIGHT = epsimplelib.DEVICE_HEIGHT


def toPercentHeight(num):
    return num * .01 * EPD_HEIGHT


def toPercentWidth(num):
    return num * .01 * EPD_WIDTH


def display(title, msgs):
    eps = epsimplelib.EPScreen('landscape')  # eps = e-Ink Paper Screen
    if title:
        eps.set_title('From ' + title + ':')
    if len(msgs) == 1:
        width = 20
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

    eps.add_line((100, 100, 150, 100))

    eps.update_screen()

def display_image(path, title=None):
    # init display
    eps = epsimplelib.EPScreen('landscape')  # eps = e-Ink Paper Screen

    title_height = 0
    if title is not None:
        # title is 28 pixels according to epsimplelib.py
        title_height = 28
        eps.set_title(title)

    # load the image
    original = Image.open(path)
    resized = original.resize((eps.width - 1, eps.height - 1 - title_height))

    eps.image_live.paste(resized, (0, title_height))
    eps.update_screen()

def display_unicorn():
    display_image("org.png")

def display_heart():
    display_image("../heart.png")

def display_unicorn_with_title():
    display_image("org.png", "Hello world")

def main():
    display('Mattijs', ['hello world'])
    pass


if __name__ == '__main__':
    main()
