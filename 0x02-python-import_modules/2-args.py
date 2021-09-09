#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    index = len(argv) - 1

    if index == 0:
        print("{} arguments. ".format(index))

    elif index == 1:
        print("{} argument: ".format(index))

    else:
        print("{} arguments: ".format(index))

    if index >= 1:
        index = 0
        for evaAr in argv[0:]:
            if index != 0:
                print("{}: {}".format(index, evaAr))
            index += 1
