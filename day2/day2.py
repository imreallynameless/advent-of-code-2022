def day2(file):
    sum = 0
    with open(file, "r") as f:
        d = {'X': 'R', 'Y' : 'P', 'Z': 'S', 'A': 'R', 'B': 'P', 'C': 'S'}
        for line in f:
            opp, you = line.strip().split()
            you = d[you]
            opp = d[opp]

            if you == 'R':
                if opp == 'R':
                    sum += 3
                elif opp == 'P':
                    sum += 1
                else:
                    sum += 2

            if you == 'P':
                if opp == 'R':
                    sum += 1
                elif opp == 'P':
                    sum += 2
                else:
                    sum += 3
                sum += 3
            if you == 'S':
                if opp == 'R':
                    sum += 2
                elif opp == 'P':
                    sum += 3
                else:
                    sum += 1
                sum += 6

            # if you == opp:
            #     sum += 3
            # if (you == 'R' and opp == 'S') or (you == 'P' and opp == 'R') or (you == 'S' and opp == 'P'):
            #     sum += 6
        

    return sum

print(day2('input.txt'))