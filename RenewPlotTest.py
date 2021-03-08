import numpy as np
import matplotlib.pyplot as plt
import time


def reNewAxis(new_y):
    print(new_y)
    l.set_ydata(new_y)
    plt.draw()


def autoScaleAxis():
    tmpX = l.get_xdata
    tmpY = l.get_ydata
    plt.axes([np.min(tmpX), np.max(tmpX)], [np.min(tmpY), np.max(tmpY)])


# plt.ion()
fig, ax = plt.subplots()

x = np.arange(0, 1, 0.01)
y = np.cos(x)
l, = ax.plot(x, y)

tmp = y

while True:
    time.sleep(3)
    tmp = tmp*y
    reNewAxis(tmp)
    plt.draw()
    plt.pause(0.01)
    autoScaleAxis()


plt.show()