##################################################
# P26 ----> Relay_Ch1
# P20 ----> Relay_Ch2
# P21 ----> Relay_Ch3
##################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

RELAY_CH_1 = 26
RELAY_CH_2 = 20
RELAY_CH_3 = 21


def turn_on_pump(pin_number, duration):
    """
    Turn on the given pin number for the duration
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #GPIO.setup(Relay_Ch1,GPIO.OUT)
    #GPIO.setup(Relay_Ch2,GPIO.OUT)
    GPIO.setup(Relay_Ch3, GPIO.OUT)

    print(GPIO.LOW)
    print(GPIO.HIGH)
    print("Setup The Relay Module is [success]")

    #Control the Channel 1
    GPIO.output(Relay_Ch3, GPIO.LOW)
    print("Channel 1:The Common Contact is access to the Normal Open Contact!")
    time.sleep(duration)

    GPIO.output(Relay_Ch3, GPIO.HIGH)
    print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
    time.sleep(0.5)

    GPIO.cleanup()

    return

