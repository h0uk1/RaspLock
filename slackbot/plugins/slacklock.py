# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
import RPi.GPIO as GPIO
import time

PORT_R = 3
PORT_G = 2
SERVO = 18
SWITCH = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
ports = [PORT_R, PORT_G]
for port in ports:
    GPIO.setup(port, GPIO.OUT)

def set_color(r,g):
    GPIO.output(PORT_R, r)
    GPIO.output(PORT_G, g)

key = "open"
set_color(0,1)

def open_key():
        global key
        GPIO.setup(SERVO, GPIO.OUT)
        servo = GPIO.PWM(SERVO, 50)
        servo.start(0)
        servo.ChangeDutyCycle(2.5)
        time.sleep(0.5)
        servo.ChangeDutyCycle(7.25)
        time.sleep(0.5)
        set_color(0, 1)
        key = "open"
        servo.stop()

def close_key():
        global key
        GPIO.setup(SERVO, GPIO.OUT)
        servo = GPIO.PWM(SERVO, 50)
        servo.start(0)
        servo.ChangeDutyCycle(12)
        time.sleep(0.5)
        servo.ChangeDutyCycle(7.25)
        time.sleep(0.5)
        set_color(1, 0)
        key = "close"
        servo.stop()

def _key():
    global key
    if key == "close":
        open_key()
    if key == "open":
        close_key()

@respond_to('あけて|開けて')
@listen_to('あけて|開けて')
def open_func(message):
    global key
    if key == "close":
        open_key()
        message.reply('解錠しました')
    else:
        message.reply("開いているようです")

@respond_to('しめて|閉めて')
@listen_to('しめて|閉めて')
def close_func(message):
    global key
    if key == "open":
        close_key()
        message.reply('閉めました')
    else:
        message.reply("閉まってるようです")

@respond_to('かくにん|確認')
@listen_to('かくにん|確認')
def check_key(message):
    global key
    if key == "open":
        message.reply('開いています')
    else:
        message.reply("閉まってします")

