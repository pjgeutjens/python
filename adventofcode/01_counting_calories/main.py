counter = 1
top = 1
max = 0
total = 0
totals = []
def get_largest(input, n):
    return sorted(input, reverse=True)[:n]

with open("input.txt", 'r') as fp:
    while True:
        line = fp.readline()
        if not line:
            if total > 0:
                totals.append(total)
            break
        if line == "\n" or line == "":
            if total > max:
                top = counter
                max = total
            counter += 1
            totals.append(total)
            total = 0
        else:
            total += int(line)

result = get_largest(totals, 3)
print(result)
print(sum(result))

print("max {} at position {}".format(max, top))
