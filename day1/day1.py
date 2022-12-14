def day1(file):
    max = 0
    max2 = 0
    max3 = 0
    current = 0
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line == "":
                if current >= max:
                    max3 = max2
                    max2 = max
                    max = current
                elif current >= max2:
                    max3 = max2
                    max2 = current
                elif current >= max3:
                    max3 = current
                current = 0
            else:
                current += int(line)
                

    
    return max + max2 + max3

# def day1part2(file):
#     max = 0
#     current = 0
#     with open(file) as f:
#         data = f.readlines()
#         for line in data:
#             if line == '\n':
#                 current = 0
#             else:
#                 current += int(line)
#             if current > max:
#                 max = current
    
#     return max

print(day1('input.txt'))