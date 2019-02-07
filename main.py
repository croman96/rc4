import fileinput
import math

def main():
    instructions = []
    for line in fileinput.input():
        try:
            instructions.append(line[:-1])
        except:
            break

if __name__ == '__main__':
    main()
