def get_marker(input, window):
    for i in range(len(input) - window):
        buf = input[i:i+window]
        s = set(buf)
        if len(s) == window:
            return i + window
    return -1


with open("hard.txt", 'r') as f:
    while True:
        l = f.readline()
        if not l or l == '\n':
            exit()
        print(f'{l}: {get_marker(l, 14)}')