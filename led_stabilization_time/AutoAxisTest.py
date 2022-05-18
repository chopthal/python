import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 101, dtype=np.int8)
y = x

fig, ax = plt.subplots()
line1, = plt.plot(x, y)

for i in x:
    x = np.append(x, x[-1]+1)
    y = np.power(x, i)
    line1.set_xdata(x)
    line1.set_ydata(y)
    # plt.xlim(np.min(x), np.max(x))
    # plt.ylim(np.min(y), np.max(y))
    plt.axis([np.min(x), np.max(x), np.min(y), np.max(y)])
    plt.pause(2)


plt.show()