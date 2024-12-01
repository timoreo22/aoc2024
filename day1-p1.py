
def main():
    f = open('day1-input.txt')
    left_list = []
    right_list = []
    total = 0
    for l in f.readlines():
        ar = l.split('   ')
        if len(ar) != 2:
            continue
        left_list.append(int(ar[0]))
        right_list.append(int(ar[1]))
    f.close()
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    while len(left_list) != 0:
        total += abs(left_list.pop() - right_list.pop())
    print(total)



if __name__ == '__main__':
    main()