# GPIOなど必要なモジュールを宣言
import RPi.GPIO as GPIO
import time

S = 18
LED = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

GPIO.setup(S, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(LED, GPIO.LOW)
try:
    while True:
        if(GPIO.input(S) == GPIO.HIGH):
            print("high")
            GPIO.output(LED, GPIO.HIGH)
        else:
            print("low")
            GPIO.output(LED, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleenup()
