import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#set GPIO Pins

#set water pump

waterPin = 17
GPIO.setup(waterPin, GPIO.OUT)
GPIO.output(waterPin,GPIO.LOW)

time.sleep(5)

GPIO.output(waterPin,GPIO.HIGH)
GPIO.cleapup()
