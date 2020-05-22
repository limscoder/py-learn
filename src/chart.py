import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker

data = [
    ['2018-06-01', 100],
    ['2018-06-02', 101],
    ['2018-06-03', 102],
    ['2018-06-04', 100],
    ['2018-06-05', 105],
    ['2018-06-06', 106],
]

def draw():
    nd = np.array(data)
    t = nd[:, 0].astype('O')
    s = nd[:, 1]

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='date', ylabel='Y',
        title='A plot')
    ax.grid()
    plt.show()
