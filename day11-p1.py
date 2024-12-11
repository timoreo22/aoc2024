from math import log10, floor

def main():
    f = open("day11-input.txt")
    rocks = [int(x) for x in f.read().strip().split()]
    for _ in range(25):
        i = 0
        while i < len(rocks):
            num = rocks[i]
            if num == 0:
                rocks[i] = 1
            else:
                digits = int(log10(num)) + 1
                if round(digits % 2) == 0:
                    mult = 10 ** (digits / 2)
                    l = floor(num / mult)
                    rocks[i] = l
                    tot = int(num - (l * mult))
                    rocks.insert(i + 1, tot)
                    i += 1
                else:
                    rocks[i] = num * 2024
            i += 1
    print(len(rocks))
    f.close()

if __name__ == '__main__':
    main()