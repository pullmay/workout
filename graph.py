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
        sec_str = e[-6:].replace(' |\n', '')
        seconds.append(int(sec_str))
    
    return seconds

if __name__ == "__main__":
    y = get_seconds()
    x = list(range(1, len(y) + 1))
    plt.figure(0)
    plt.title('My Work Out Memo')
    plt.xlabel('Times')
    plt.ylabel('Seconds')
    plt.plot(x, y, color='blue', linestyle='solid', linewidth = 1.0, marker='o')
    plt.show()