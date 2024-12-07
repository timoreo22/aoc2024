def main():
    f = open("day7-input.txt")
    total = 0
    for line in f.readlines():
        values = line.split()
        result = int(values.pop(0)[:-1])
        operands: list[int] = [int(x) for x in values]
        # add
        is_correct = False
        for i in range(3**(len(operands)-1)):
            sub_total = operands[0]
            for j in range(1,len(operands)):
                if i % 3 == 0:
                    sub_total += operands[j]
                elif i % 3 == 1:
                    sub_total *= operands[j]
                else:
                    sub_total = int(str(sub_total) + str(operands[j]))
                i //= 3
            if sub_total == result:
                is_correct = True
                break
        if is_correct:
            total += result
    print(total)


    f.close()

if __name__ == '__main__':
    main()