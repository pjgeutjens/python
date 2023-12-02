import string


class Group:
    rucksacks = []

    def __init__(self, rucksacks) -> None:
        self.rucksacks = rucksacks

    def add(self, rucksack):
        self.rucksacks.append(rucksack.strip())

    def common(self):
        if len(self.rucksacks) == 0:
            return ""
        result = set(self.rucksacks[0])
        for r in self.rucksacks:
            result = result.intersection(set(r))
        print(result)
        return list(result)[0]


class Rucksack:
    contents = ""
    compartments = []

    def __init__(self, contents):
        self.contents = contents
        self.compartments = [
            self.contents[: len(self.contents) // 2],
            self.contents[len(self.contents) // 2 :],
        ]

    def common(self):
        print(set(self.compartments[0]))
        print(set(self.compartments[1]))
        return list(set(self.compartments[0]).intersection(set(self.compartments[1])))[
            0
        ]


def priority(char):
    if not char.isalpha():
        return 0
    lookup = string.ascii_lowercase + string.ascii_uppercase
    return lookup.index(char) + 1


score = 0

with open("hard.txt", "r") as bags:
    counter = 0
    while True:
        g = Group([])
        for member in range(3):
            bag = bags.readline()
            # print(turn)
            if not bag:
                print("total: {}".format(score))
                exit()
            if bag == "\n":
                continue
            g.add(bag)
        score += priority(g.common())

