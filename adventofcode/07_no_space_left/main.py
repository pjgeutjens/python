class Directory:
    parent = None
    children = []
    files = []
    total_size = 0


class File:
    directory: Directory
    size: int


class CommandLine:
    pwd = None
    directories = []
    known_commands = ['cd', 'ls']
    @classmethod
    def parse(cls, input, line):
        print(f'parsing {line}')
        if not line.startswith('$'):
            return
        parts = line.lstrip('$').strip().split(' ')
        cls.handle_output(input, parts)

    @classmethod
    def handle_output(cls, input, parts, pwd):
        cmd = parts[0]
         



class Filesystem:
    pwd = None
    directories = {}


with open("simple.txt", 'r') as f:
    while True:
        l = f.readline()
        if not l or l == '\n':
            exit()
        CommandLine.parse(f, l)
