import PySimpleGUI as sg
import RPi.GPIO as GPIO
import time
import multiprocessing


GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

#Sensors for Water Level Sensor
#GPIO_TRIGGER =
#GPIO_ECHO =
#GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#GPIO.setup(GPIO_ECHO, GPIO.IN)
#GPIOPin =
#GPIO.setup(GPIOPin, GPIO.OUT)

#Sensors for Staion 1
GPIO_TRIGGER1 = 3
GPIO_ECHO1 = 2
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIOPin1 =17
GPIO.setup(GPIOPin1, GPIO.OUT)
GPIO.output(GPIOPin1, GPIO.HIGH)

#Sensors for Station 2
GPIO_TRIGGER2 =15
GPIO_ECHO2 =14
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIOPin2 =27
GPIO.setup(GPIOPin2, GPIO.OUT)
GPIO.output(GPIOPin2, GPIO.HIGH)

#Sensors for Station 3
GPIO_TRIGGER3 =24
GPIO_ECHO3 =23
GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
GPIO.setup(GPIO_ECHO3, GPIO.IN)
GPIOPin3 =10
GPIO.setup(GPIOPin3, GPIO.OUT)
GPIO.output(GPIOPin3, GPIO.HIGH)

#Sensors for Station 4
GPIO_TRIGGER4 =8
GPIO_ECHO4 =25
GPIO.setup(GPIO_TRIGGER4, GPIO.OUT)
GPIO.setup(GPIO_ECHO4, GPIO.IN)
GPIOPin4 =22
GPIO.setup(GPIOPin4, GPIO.OUT)
GPIO.output(GPIOPin4, GPIO.HIGH)


def waterLevel():
    stop = False

    while stop == False:

        #dist = distance(GPIO_TRIGGER, GPIO_ECHO)

        time.sleep(5)

        waterOn(GPIOPin)

        time.sleep(2)

        waterOff(GPIOPin)

        if dist >= 5:
            stop = True


def waterOn(Pin):
    GPIO.output(Pin, GPIO.LOW)


def waterOff(Pin):
    GPIO.output(Pin, GPIO.HIGH)


def distance(GPIO_Trigger, GPIO_ECHO):
    #keepGoing = True
    print('distance called')
    #while keepGoing == True:
    GPIO.output(GPIO_Trigger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_Trigger, False)

    StartTime = time.time()
    StopTime = time.time()
    #print('89')
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    #print('93')
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    #print('97')
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back

    distance = (TimeElapsed * 34300) / 2
    print('dist from fucntion; ',distance)
    return distance


def waterStation1():
    stop = False
    dist = distance(GPIO_TRIGGER1, GPIO_ECHO1)

    if dist <= 10:
            stop = True

    while stop == False:

        waterOn(GPIOPin1)
        time.sleep(2)
        

        GPIO.output(GPIOPin1, GPIO.HIGH) #water off
        time.sleep(.5)
        dist = distance(GPIO_TRIGGER1, GPIO_ECHO1)
        if dist <= 10:
            stop = True
            GPIO.output(GPIOPin1, GPIO.HIGH)


def waterStation2():
    stop = False
    dist = distance(GPIO_TRIGGER2, GPIO_ECHO2)

    if dist <= 10:
            stop = True

    while stop == False:

        waterOn(GPIOPin2)
        time.sleep(2)
        

        GPIO.output(GPIOPin2, GPIO.HIGH) #water off
        time.sleep(.5)
        dist = distance(GPIO_TRIGGER2, GPIO_ECHO2)
        if dist <= 10:
            stop = True
            GPIO.output(GPIOPin2, GPIO.HIGH)


def waterStation3():
    stop = False
    dist = distance(GPIO_TRIGGER3, GPIO_ECHO3)
    if dist <= 10:
            stop = True

    while stop == False:

        dist = distance(GPIO_TRIGGER3, GPIO_ECHO3)

        

        waterOn(GPIOPin3)
        time.sleep(5)

        GPIO.output(GPIOPin3, GPIO.HIGH) #water off
        time.sleep(1)
        dist = distance(GPIO_TRIGGER3, GPIO_ECHO3)
        if dist <= 10:
            stop = True


def waterStation4():
    stop = False
    dist = distance(GPIO_TRIGGER4, GPIO_ECHO4)

    if dist <= 10:
            stop = True

    while stop == False:

        waterOn(GPIOPin4)
        time.sleep(2)
        

        GPIO.output(GPIOPin4, GPIO.HIGH) #water off
        #time.sleep(1)
        dist = distance(GPIO_TRIGGER4, GPIO_ECHO4)
        if dist <= 10:
            stop = True
            GPIO.output(GPIOPin4, GPIO.HIGH)


def waterStationAll():
    #waterStation1()
    #waterStation2()
    #waterStation3()
    #waterStation4()
    p1 = multiprocessing.Process(target=waterStation1, args=())
    p2 = multiprocessing.Process(target=waterStation2, args=())
    p3 = multiprocessing.Process(target=waterStation3, args=())
    p4 = multiprocessing.Process(target=waterStation4, args=())
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()


def fillFunc(message):
    if message =="1":
        p1 = multiprocessing.Process(target=waterStation1, args=())
        p1.start()
    if message =="2":
        p2 = multiprocessing.Process(target=waterStation2, args=())
        p2.start()
    if message =="3":
        p3 = multiprocessing.Process(target=waterStation3, args=())
        p3.start()
    if message =="4":
        p4 = multiprocessing.Process(target=waterStation4, args=())
        p4.start()
    if message =="All":
        p5 = multiprocessing.Process(target=waterStationAll, args=())
        p5.start()

layout = [[sg.Text("Alerts", background_color = "white",text_color="black",justification ="left",font = ("Helvetica", 30),key = "alert"),sg.Graph(canvas_size=(50,50),graph_bottom_left=(0, 0),graph_top_right=(50,50),key = "graph", background_color = "white",pad=((5,0),3)),sg.Text("Water Tank Needs to be Filled",background_color= "#800000",text_color="white",k="banner",font = ("Helvetica", 31),pad=((0,5),3))],
          [sg.Text("Water Stations", background_color = "white",text_color="black",size= (20,1),justification = "right",font = ("Helvetica", 30)),sg.Button("Select All",button_color  = "#800000",font = ("Helvetica", 30))],
          [sg.Button("1",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("2",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("3",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("4",button_color  = "#800000",font = ("Helvetica", 90))]]

window = sg.Window("Liquid Dispenser", layout, element_justification='c', background_color = "white").Finalize()
graph = window.Element("graph")
graph.draw_polygon([(0,25),(50,0),(50,50)], fill_color="#800000")
window["graph"].update()
window["graph"].update(visible =False)
window["banner"].update(visible=False)
window["alert"].update(visible=False)


while True:
    if True:
        window["graph"].update(visible =False)
        window["banner"].update(visible=False)
        window["alert"].update(visible=False)
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '1':
        fillFunc("1")
    if event == '2':
        fillFunc("2")
    if event == '3':
        fillFunc("3")
    if event == '4':
        fillFunc("4")
    if event == 'Select All':
        fillFunc("All")

window.close()
