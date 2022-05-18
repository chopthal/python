import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, CheckButtons
# import time


# Variables


# Definitions

class BtnActions:

    def __init__(self):
        self.stopFlag = 0

    def StartWOPlot(self):
        print('StartWOPlot_Clicked')

    def Start(self):
        self.stopFlag = 0
        print('Start_Clicked')
        x = []
        y = []
        tmpX = []
        # tmpY = []
        t = 0
        line1, = ax.plot(x, y)

        while self.stopFlag == 0:
            tmpX.append(t)
            # tmpY = tmpX * 2
            x = np.array(tmpX)
            y = np.power(x, 2)

            line1.set_xdata(x)
            line1.set_ydata(y)

            plt.axis([np.min(x), np.max(x), np.min(y), np.max(y)])
            # plt.draw()
            plt.pause(1)
            t = t + 0.01

    def Stop(self):
        print('Stop_Clicked')
        self.stopFlag = 1

    def LED1(self):
        print('LED1_Clicked')

    def LED2(self):
        print('LED2_Clicked')

    def LEDOff(self):
        print('LEDOff_Clicked')


# plt.ion()
fig = plt.figure(1)
ax = plt.plot(211)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2, top=0.9)


# Make Buttons
axBtnStartWOPlot = plt.axes([0.16, 0.05, 0.2, 0.075])
btnStartWOPlot = Button(axBtnStartWOPlot, 'Start W/O Plot')
btnStartWOPlot.on_clicked(BtnActions.StartWOPlot)

axBtnStart = plt.axes([0.37, 0.05, 0.1, 0.075])
btnStart = Button(axBtnStart, 'Start')
btnStart.on_clicked(BtnActions.Start)

axBtnStop = plt.axes([0.48, 0.05, 0.1, 0.075])
btnStop = Button(axBtnStop, 'Stop')
btnStop.on_clicked(BtnActions.Stop)

axBtnLED1 = plt.axes([0.59, 0.05, 0.1, 0.075])
btnLED1 = Button(axBtnLED1, 'LED1')
btnLED1.on_clicked(BtnActions.LED1)

axBtnLED2 = plt.axes([0.7, 0.05, 0.1, 0.075])
btnLED2 = Button(axBtnLED2, 'LED2')
btnLED2.on_clicked(BtnActions.LED2)

axBtnLEDOff = plt.axes([0.81, 0.05, 0.1, 0.075])
btnLEDOff = Button(axBtnLEDOff, 'LED Off')
btnLEDOff.on_clicked(BtnActions.LEDOff)

plt.show()