import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(i):
    data = pd.read_csv("data.csv")
    x_val = data["x_value"]
    pewdipie = data["pewdipie"]
    t_series = data["t-series"]

    plt.cla()
    plt.plot(x_val, pewdipie, label="PewDiPie")
    plt.plot(x_val, t_series, label="T-Series")
    plt.ylabel("Subscriber Count")
    plt.title("Live Subscriber Plot")
    plt.tight_layout()
    plt.legend()


ani = FuncAnimation(plt.gcf(), animate)

plt.show()
