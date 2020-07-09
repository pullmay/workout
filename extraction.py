
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
    seconds = get_seconds()
    # print(seconds)