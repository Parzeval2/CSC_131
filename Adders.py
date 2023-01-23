import RPi.GPIO as GPIO
from time import sleep

def setGPIO():
    gpio = [17, 18, 27, 22, 26, 12, 16, 20, 21]
    GPIO.setup(gpio, GPIO.OUT)
    return gpio

def setNUM():
    num = []
    for i in range(0, 8):
        num.append(randint(0,1))
        return num

def display():
    for i in range(len(sum)):
        # if the i-th bit is 1, then turn the i-th LED on
        if (sum[i] == 1):
            GPIO.output(gpio[i], GPIO.HIGH)
        # otherwise, turn it off
        else:
            GPIO.output(gpio[i], GPIO.LOW)
