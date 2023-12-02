class Assignment:
    start = 0
    end = 0

    def __init__(self, plotrange):
        limits = plotrange.split('-')
        self.start = (int)(limits[0])
        self.end = (int)(limits[1])

    def contains(self, assignment):
        return self.start <= assignment.start and self.end >= assignment.end

    def overlaps(self, assignment):
        a = set(range(self.start, self.end + 1))
        b = set(range(assignment.start, assignment.end + 1))
        r = len(a.intersection(b))
        return r



counter = 0
with open("hard.txt", "r") as input:
    while True:
        pair = input.readline()
        # print(turn)
        if not pair:
            print("total: {}".format(counter))
            exit()
        if pair == "\n":
            continue

        assignments = pair.strip().split(',')
        if Assignment(assignments[0]).overlaps(Assignment(assignments[1])):
            counter += 1
