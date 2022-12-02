#!/usr/bin/python3

for i in range(0, 100):
    for j in range(i + 1, 100):
        if "{:02d}".format(j)[0] == "{:02d}".format(i)[1] and \
            "{:02d}".format(j)[1] == "{:02d}".format(i)[0]:
            if i != 89:
                print("{:02d}, ".format(i), end="")
            else:
                print("89")
    else:
        continue
