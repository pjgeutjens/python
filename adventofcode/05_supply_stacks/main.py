import re

class Stacks:
    stacks = {}
    keep = []

    def __init__(self, count):
        for i in range(1, count + 1):
            self.stacks[i] = []

    def add(self, stack, content):
        if content == "*":
            return
        self.stacks[stack].append(content)

    def set(self, stack, content):
        self.stacks[stack] = content

    def top(self, i):
        if len(self.stacks[i]) == 0:
            return '-'
        return self.stacks[i][-1]

    def tops(self):
        result = ''
        for i in range(1, len(self.stacks) + 1):
            result += f'{self.top(i)}'
        return result

    def count(self):
        return len(self.stacks)

    def __len__(self):
        return len(self.stacks)

    def __str__(self):
        details = f'{self.stacks}'
        return details

    def move(self, n, src, dest, keep = 0, focus = None, version = ''):
        print("moving {} crates from {} to {}".format(n, src, dest))
        if (len(self.keep)) < keep:
            self.keep.append(self.stacks)
        if version == 'v2':
            move = self.stacks[src][-n:]
            del self.stacks[src][-n:]
            self.stacks[dest] += move
        else:
            for i in range(n):
                if len(self.stacks[src]) == 0:
                    print(f"moving from empty stack {src}")
                    print(f"{len(self.keep)} stacks saved")
                    print(self.keep)
                t = self.stacks[src].pop()
                self.stacks[dest].append(t)
        if focus:
            print("focus")
            print(self.stacks[focus])
        # print(self)


def reverse_and_fill(infile, outfile):
    with open(infile) as f:
        txt = f.readlines()
        txt = txt[::-1]
    with open(outfile, 'w') as outf:
        for x in txt:
            if len(re.findall('\d', x)) == 0:
                x = x.replace("     ", " [*] ")
            outf.write(x)

def get_stacks_count(infile): # from the first line
    with open(infile) as f:
        header = f.readline()
        print(header)

    return int(re.findall(r'\d+', header)[-1])


def populate(s: Stacks, input):
    with open(input,'r') as f:
        f.readline() # skip the header
        while True:
            l = f.readline()
            if not l or l == '\n':
                return
            crates = re.findall('[A-Z]|\*', l)
            for i in range(len(crates)):
                s.add(i+1,crates[i])

def crane(s: Stacks, input, keep = 0, focus = None, version=''):
    count = 1
    with open(input,'r') as f:
        while True:
            print(f'on line {count}')
            count += 1
            i = f.readline()
            if not i or i == '\n':
                return
            ops = re.search('(?P<count>\d+) from (?P<src>\d+) to (?P<dest>\d+)', i)
            stack.move(int(ops.group('count')), int(ops.group('src')), int(ops.group('dest')), keep, focus, version)




# reverse_and_fill("hard.txt", "rhard.txt")
print(get_stacks_count("rhard.txt"))

stack = Stacks(get_stacks_count("rhard.txt"))
populate(stack, "rhard.txt")
print(stack)

crane(stack, "instructions.txt", 3, 6, 'v2')
print(stack)
print(stack.tops())
print("done")

