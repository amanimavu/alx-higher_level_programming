#!/usr/bin/python3.8
import re
import hidden_4


def main():
    names = dir(hidden_4)
    names.sort()
    for i in range(0, len(names)):
        if re.match(r'^_', names[i]):
            continue
        else:
            print(names[i])


if __name__ == "__main__":
    main()
