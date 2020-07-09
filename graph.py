import numpy as np
import matplotlib.pyplot as plt
from random import randint

def get_seconds():
    path = './sally_up_challenge.md'

    with open(path) as f:
        line = f.readlines()

    # 6 行目から数値が入っている
    seconds = []
    for i, e in enumerate(line):
        if i < 6: continue
        sec_str = e[8:].replace(' |\n', '')
        seconds.append(int(sec_str))
    
    return seconds

if __name__ == "__main__":
    # x = list(range(1, 10))
    # y = [randint(1, 10) for _ in x]
    y = get_seconds()
    x = list(range(1, len(y) + 1))
    plt.figure(0)
    plt.plot(x, y)
    plt.show()