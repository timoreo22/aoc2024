def is_safe(tab: list[int]):
    diff = int(tab[1]) - tab[0]
    prev = tab.pop(0)
    for el in tab:
        if diff >= 0:
            if prev + 1 <= el <= prev + 3:
                prev = el
            else:
                return False
        else:
            if prev -1 >= el >= prev -3:
                prev = el
            else:
                return False
    return True

def main():
    f = open('day2-input.txt')
    safe = 0
    for line in f.readlines():
        ar = [int(x) for x in line.split(' ')]
        for i in range(len(ar)):
            if is_safe(ar[:i] + ar[i + 1:]):
                safe += 1
                break
    f.close()
    print(safe)

if __name__ == '__main__':
    main()