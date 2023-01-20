import RPi.GPIO as GPIO
from time import sleep

inA = 25
inB = 5
outS = 17
outC = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(inA,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inB,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outS,GPIO.OUT)
GPIO.setup(outC,GPIO.OUT)

try:
    while True:
        A = 0
        B = 0
        S = 0
        C = 0

        if (GPIO.input(inA) == GPIO.HIGH):
            A = 1
        if (GPIO.input(inB) == GPIO.HIGH):
            B = 1
        S = A ^ B
        C = A & B

        GPIO.output(outS,S)
        GPIO.output(outC,C)

except KeyboardInterrupt:
    GPIO.cleanup()
