import re
def main():
    f = open('day3-input.txt')
    total = 0
    pattern = re.compile(r"mul\((\d\d?\d?),(\d\d?\d?)\)")
    line = f.read()
    f.close()
    match = re.findall(pattern, line)
    for m in match:
        total += int(m[0]) * int(m[1])
    print(total)

if __name__ == '__main__':
    main()