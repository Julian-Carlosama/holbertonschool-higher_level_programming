#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    dat = len(sys.argv) - 1

    if dat != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif dat == 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        from calculator_1 import add, sub, mul, div
        op = sys.argv[2]
        if op == "+":
            print("{} + {} = {}".format(num1, num2, add(num1, num2)))
            exit(0)
        elif op == "-":
            print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
            exit(0)
        elif op == "*":
            print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
            exit(0)
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(num1, num2, div(num1, num2)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
