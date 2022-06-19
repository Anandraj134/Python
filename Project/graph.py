# import matplotlib.pyplot as plt
# import numpy as np
#
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2*np.pi*t)
# plt.plot(t, s)
#
# plt.xlabel('time (s)')
# plt.ylabel('voltage (mV)')
# plt.title('About as simple as it gets, folks')
# plt.grid(True)
# # plt.savefig("test.png")
# plt.show()
#
import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-10,9,20)
y= x**3
z= x**2

figure = plt.figure()
axes = figure.add_axes([0,0,1,1])

axes.plot(x,z, label="Square Function")
axes.plot(x,z, label="Cube Function")
axes.legend()