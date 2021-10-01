from matplotlib import pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_value = []
y_value = []

index = count()

def animate(i):
    x_value.append(next(index))
    y_value.append(random.randint(0,5))
    
    plt.cla()
    plt.plot(x_value,y_value,label="Sensor X reading")
    plt.legend(loc="upper left")
    plt.title("Sensor X reading value")

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()