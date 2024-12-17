from tqdm import tqdm
def main():
    f = open('day17-input.txt')
    a = int(f.readline().split()[2])
    b = int(f.readline().split()[2])
    c = int(f.readline().split()[2])
    f.readline()
    instructions = [int(x) for x in f.readline().split()[1].split(',')]
    f.close()

    active = [0]
    for c_l in range(len(instructions)):
        backup = active
        active = []
        for c in backup:
            for d in range(8):
                a = 8 * c + d
                if find_output(a, instructions) == instructions[-c_l - 1:]:
                    active.append(a)
    print(min(active))


def find_output(a, instructions):
    b = 0
    c = 0
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
    output = []
    while rip < len(instructions) - 1:
        match instructions[rip]:
            case 0:
                a = int(a / (1 << get_combo(instructions[rip + 1])))
            case 1:
                b = b ^ instructions[rip + 1]
            case 2:
                b = get_combo(instructions[rip + 1]) % 8
            case 3:
                if a != 0:
                    rip = instructions[rip + 1]
                    continue  # skip incrementing
            case 4:
                b = b ^ c
            case 5:
                output.append(get_combo(instructions[rip + 1]) % 8)
            case 6:
                b = int(a / (1 << get_combo(instructions[rip + 1])))
            case 7:
                c = int(a / (1 << get_combo(instructions[rip + 1])))
            case _:
                print("SIGILL")
        rip += 2
    return output


if __name__ == '__main__':
    main()