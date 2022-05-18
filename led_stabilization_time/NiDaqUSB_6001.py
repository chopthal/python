import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, CheckButtons
import time
import serial
import nidaqmx


# Variables
baudRate = 9600
comPort = 'COM5'
ser = serial.Serial(comPort, baudRate)
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.parity = serial.PARITY_NONE
ser.timeout = 1
tGap = 10 # ms
tPause = 10 # ms


# Definitions
def SerialConnection():

    try:
        ser.open()
    except:
        ser.close()
        ser.open()

    ser.flushInput()
    ser.flushOutput()

    proStr = '$D#NAME'
    endStr = '\r'  # CR

    TX = proStr + endStr
    TX = TX.encode()
    RX = ''
    wantRX = proStr + '#Maximultix#OK' + endStr

    t = time.time()
    t1 = 0

    while wantRX != RX and t1 < 5:
        ser.write(TX)
        # RX = ser.read_until(terminator='\r').decode()
        RX = ser.read_until(expected='\r').decode()
        t1 = time.time() - t

    if wantRX == RX:
        print('Connected Successfully!')
        print('Device Name = ' + RX)
    else:
        print('Connection Failed!')


def serialCommunication(proStr):
    ser.flushInput()
    ser.flushOutput()
    endStr = '\r'  # CR

    TX = proStr + endStr
    TX = TX.encode()
    RX = ''
    wantRX = proStr + '#Maximultix#OK' + endStr

    t = time.time()
    t1 = 0

    while wantRX != RX and t1 < 5:
        ser.write(TX)
        # RX = ser.read_until(terminator='\r').decode()
        RX = ser.read_until(expected='\r').decode()
        t1 = time.time() - t

    if wantRX == RX:
        print('Communicate Successfully!')
        print('Return = ' + RX)
    else:
        print('Communication Failed!')


def StartWOPlot(event):
    print('StartWOPlot_Clicked')
    tmpX = []
    tmpY = []

    while True:
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(("Dev1/ai0"))
            res = task.read(number_of_samples_per_channel=1)

            tmpX.append(t)
            tmpY.append(res)

            time.sleep(tGap / 1000)
            t = t + tGap


def Start(event):
    print('Start_Clicked')
    x = []
    y = []
    tmpX = []
    tmpY = []
    t = 0
    line1, = ax.plot(x, y)

    while True:
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(("Dev1/ai0"))
            res = task.read(number_of_samples_per_channel=1)

        tmpX.append(t)
        tmpY.append(res)
        x = np.array(tmpX)
        y = np.array(tmpY)

        line1.set_xdata(x)
        line1.set_ydata(y)
        plt.draw()
        plt.pause(tPause / 1000)

        time.sleep(tGap / 1000)
        t = t + tGap


def Stop(event):
    print('Stop_Clicked')
    return False


def LED1(event):
    print('LED1_Clicked')
    serialCommunication('$L#1#ON#100')


def LED2(event):
    print('LED2_Clicked')
    serialCommunication('$L#2#ON#100')


def LEDOff(event):
    print('LEDOff_Clicked')
    serialCommunication('$L#1#OFF')
    serialCommunication('$L#2#OFF')


plt.ion()
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2, top=0.9)


# Make Buttons
axBtnStartWOPlot = plt.axes([0.16, 0.05, 0.2, 0.075])
btnStartWOPlot = Button(axBtnStartWOPlot, 'Start W/O Plot')
btnStartWOPlot.on_clicked(StartWOPlot)

axBtnStart = plt.axes([0.37, 0.05, 0.1, 0.075])
btnStart = Button(axBtnStart, 'Start')
btnStart.on_clicked(Start)

axBtnStop = plt.axes([0.48, 0.05, 0.1, 0.075])
btnStop = Button(axBtnStop, 'Stop')
btnStop.on_clicked(Stop)

axBtnLED1 = plt.axes([0.59, 0.05, 0.1, 0.075])
btnLED1 = Button(axBtnLED1, 'LED1')
btnLED1.on_clicked(LED1)

axBtnLED2 = plt.axes([0.7, 0.05, 0.1, 0.075])
btnLED2 = Button(axBtnLED2, 'LED2')
btnLED2.on_clicked(LED2)

axBtnLEDOff = plt.axes([0.81, 0.05, 0.1, 0.075])
btnLEDOff = Button(axBtnLEDOff, 'LED Off')
btnLEDOff.on_clicked(LEDOff)


plt.show()