def day1(file):
    max = 0
    with open(file) as f:
        data = f.readlines()
        for line in data:
            print(line)
            current = 0
            if line == '/n':
                current = 0
            else:
                current += int(line)
            if current > max:
                max = current
    
    return max

print(day1('input.txt'))