import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Sensors for Water Level Sensor
GPIO_TRIGGER = 
GPIO_ECHO = 
#For water pin
GPIOPin = 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIOPin, GPIO.OUT)

#Sensors for Staion 1
GPIO_TRIGGER1 = 
GPIO_ECHO1 = 
GPIOPin1 = 
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIOPin1, GPIO.OUT)

#Sensors for Station 2
GPIO_TRIGGER2 = 
GPIO_ECHO2 = 
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIOPin2 = 
GPIO.setup(GPIOPin2, GPIO.OUT)

#Sensors for Station 3
GPIO_TRIGGER3 = 
GPIO_ECHO3 = 
GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)
GPIOPin3 = 
GPIO.setup(GPIOPin3, GPIO.OUT)

#Sensors for Station 4
GPIO_TRIGGER4 = 
GPIO_ECHO4 = 
GPIO.setup(GPIO_TRIGGER4, GPIO.OUT)
GPIO.setup(GPIO_ECHO4, GPIO.IN)
GPIOPin4 = 
GPIO.setup(GPIOPin4, GPIO.OUT)

def waterLevel():



def waterOn(Pin):

	GPIO.output(Pin,True)

def waterOff(Pin):
	GPIO.output(Pin,False)	

def distance(GPIO_Trigger, GPIO_ECHO, Pin):

	keepGoing = True

	while keepGoing == True:

		GPIO.output(GPIO_TRIGGER, True)

    	# set Trigger after 0.01ms to LOW
    	time.sleep(0.00001)
    	GPIO.output(GPIO_TRIGGER, False)

    	StartTime = time.time()
    	StopTime = time.time()

    	# save StartTime
    	while GPIO.input(GPIO_ECHO) == 0:
        	StartTime = time.time()

    	# save time of arrival
    	while GPIO.input(GPIO_ECHO) == 1:
        	StopTime = time.time()

    # time difference between start and arrival
    	TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back

    	distance = (TimeElapsed * 34300) / 2

    	waterOn(Pin)

    	if distance == 5:
    		waterOff(Pin)
    		keepGoing = False

return 

def waterStation1(TRIGGER,ECHO,Pin):

	stop = False

	while stop == False: 

		dist = distance(TRIGGER, ECHO, Pin)

		time.sleep(5)

		waterOn(Pin)

		time.sleep(2)

		waterOff(Pin)

		if dist == 5:

			stop = True

def waterStation2(TRIGGER,ECHO,Pin):
	stop = False

	while stop == False: 

		dist = distance(TRIGGER, ECHO, Pin)

		time.sleep(5)

		waterOn(Pin)

		time.sleep(2)

		waterOff(Pin)

		if dist == 5:

			stop = True
	

def waterStation3(TRIGGER,ECHO,Pin):
	stop = False

	while stop == False: 

		dist = distance(TRIGGER, ECHO, Pin)

		time.sleep(5)

		waterOn(Pin)

		time.sleep(2)

		waterOff(Pin)

		if dist == 5:

			stop = True

def waterStation4(TRIGGER,ECHO,Pin):
	stop = False

	while stop == False: 

		dist = distance(TRIGGER, ECHO, Pin)

		time.sleep(5)

		waterOn(Pin)

		time.sleep(2)

		waterOff(Pin)

		if dist == 5:

			stop = True

def waterStationAll():
	waterStation1()
	waterStation2()
	waterStation3()
	waterStation4()