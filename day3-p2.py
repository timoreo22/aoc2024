import re
def main():
    f = open('day3-input.txt')
    total = 0
    pattern = re.compile(r"mul\((\d\d?\d?),(\d\d?\d?)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")
    cur_m = True
    line = f.read()
    f.close()
    match = re.finditer(pattern, line)
    do_match = [x.start() for x in re.finditer(do_pattern, line)]
    dont_match = [x.start() for x in re.finditer(dont_pattern, line)]
    #sections 97529391
    for m in match:
        i = m.start()
        if (len(do_match) > 0 and i > do_match[0]) or (len(dont_match) > 0 and i > dont_match[0]):
            if(len(do_match)) == 0:
                cur_m = False
                dont_match.pop(0)
            elif len(dont_match) == 0:
                cur_m = True
                do_match.pop(0)
            elif do_match[0] > dont_match[0]:
                cur_m = False
                dont_match.pop(0)
            else:
                cur_m = True
                do_match.pop(0)
        if cur_m:
            total += int(m.group(1)) * int(m.group(2))
    print(total)

if __name__ == '__main__':
    main()