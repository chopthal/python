import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt
import serial
from matplotlib.widgets import Button
from pynput.keyboard import Listener, Key


baudRate = 9600
comPort = 'COM5'
ser = serial.Serial(comPort, baudRate)
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.parity = serial.PARITY_NONE

ser.timeout = 1

try:
    ser.open()
except:
    ser.close()
    ser.open()

ser.flushInput()
ser.flushOutput()

proStr = '$D#NAME'
endStr = '\r' # CR

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


startTime = time.time()

tDur = 100000 # ms
tGap = 10 # ms
tPause = 10 # ms
tmpX = []
tmpY = []
x = []
y = []

plt.ion()
fig = plt.figure()
sf = fig.add_subplot()
line1, = sf.plot(x, y)

t = 0
while t < tDur:

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(("Dev1/ai0"))
        res = task.read(number_of_samples_per_channel=1)

    tmpX.append(t)
    tmpY.append(res)
    x = np.array(tmpX)
    y = np.array(tmpY)
    # plt.cla()
    # plt.plot(x, y)
    line1.set_xdata(x)
    line1.set_ydata(y)
    plt.draw()
    plt.pause(tPause/1000)

    time.sleep(tGap/1000)
    # t = t + tGap
    t = t + tGap + tPause

endTime = time.time() - startTime
print(endTime)

plt.show()