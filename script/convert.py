from roman_arabic_numerals import conv
import sys


def main():
    # read from stdin
    for line in sys.stdin:
        if line.strip() == "":
            print(line.strip())
        else:
            if line.startswith("##"):
                tokens = line.split()
                newline = []
                newline.append(tokens[0])
                newline.append(str(conv.rom_arab(tokens[1])))
                # put all the other tokens in the new line
                newline.extend(tokens[2:])
                print(" ".join(newline).strip())
            else:
                print(line.strip())


if __name__ == "__main__":
    main()
