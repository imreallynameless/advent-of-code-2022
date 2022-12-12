def day2(file):
    sum = 0
    with open(file) as f:
        data = f.readlines()
        for line in data:
            line = line.split()
            line = list(map(int, line))
            sum += max(line) - min(line)
    return sum

print(day2('input.txt'))