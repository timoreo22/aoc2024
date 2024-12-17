def main():
    f = open('day17-input.txt')
    a = int(f.readline().split()[2])
    b = int(f.readline().split()[2])
    c = int(f.readline().split()[2])
    print(a,b,c)
    f.readline()
    instructions = [int(x) for x in f.readline().split()[1].split(',')]
    print(instructions)
    f.close()
    rip = 0

    def get_combo(i):
        if i <= 3:
            return i
        elif i == 4:
            return a
        elif i == 5:
            return b
        elif i == 6:
            return c
        elif i == 7:
            print('Error reserved combo')
            pass  # reserved
        print("Error, didn't match any combo")
    output = ""
    while rip < len(instructions)-1:
        match instructions[rip]:
            case 0:
                a = int(a / (2.0 ** get_combo(instructions[rip + 1])))
            case 1:
                b = b ^ instructions[rip + 1]
            case 2:
                b = get_combo(instructions[rip + 1]) % 8
            case 3:
                if a != 0:
                    rip = instructions[rip + 1]
                    continue # skip incrementing
            case 4:
                b = b ^ c
            case 5:
                output += str(get_combo(instructions[rip + 1]) % 8) + ","
            case 6:
                b = int(a / (2 ** get_combo(instructions[rip + 1])))
            case 7:
                c = int(a / (2 ** get_combo(instructions[rip + 1])))
            case _:
                print("SIGILL")
        rip += 2
    print(rip)
    print(output)

if __name__ == '__main__':
    main()