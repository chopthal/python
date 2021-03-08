import serial
import time

baudRate = 9600
comPort = 'COM3'
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
    RX = ser.read_until(terminator='\r').decode()
    t1 = time.time() - t

if wantRX == RX:
    print('Connected Successfully!')
    print('Device Name = ' + RX)
else:
    print('Connection Failed!')

ser.close()