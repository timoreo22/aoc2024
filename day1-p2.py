from collections import Counter

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
    total_dict = Counter(right_list)
    while len(left_list) != 0:
        to_search = left_list.pop()
        if to_search in total_dict:
            total += to_search * total_dict[to_search]
    print(total)



if __name__ == '__main__':
    main()