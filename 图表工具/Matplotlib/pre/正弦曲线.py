import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

x = np.linspace(0, 20, 500)
y = np.sin(x)

plt.grid()

plt.plot(x, y)
plt.show()
