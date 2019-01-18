# GPIOなど必要なモジュールを宣言
import RPi.GPIO as GPIO
import time

PORT_R = 3
PORT_G = 2

SERVO = 18

SWITCH = 10

key = "open"


GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
ports = [PORT_R, PORT_G]
for port in ports:
    GPIO.setup(port, GPIO.OUT)



def set_color(r,g):
    GPIO.output(PORT_R, r)
    GPIO.output(PORT_G, g)

def open_key():
        global key
        GPIO.setup(SERVO, GPIO.OUT)
        servo = GPIO.PWM(SERVO, 50)
        servo.start(0)
        servo.ChangeDutyCycle(3)
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

def function():
    global key
    if GPIO.input(SWITCH) == GPIO.HIGH:
        if key == "open":
            close_key()
            print("close")
        elif key == "close":
            open_key()
            print("open")

while True:
    try:
        global key
        if GPIO.input(SWITCH) == GPIO.HIGH:
            if key == "open":
                close_key()
                print("close")
            elif key == "close":
                open_key()
                print("open")

        time.sleep(0.1)
    except KeyboardInterrupt:
        break
        GPIO.cleanup()
