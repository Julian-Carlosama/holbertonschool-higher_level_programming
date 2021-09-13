#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    dat = len(sys.argv) - 1
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[-1])
    suma = calculator_1.add(num1, num2)
    resta = calculator_1.sub(num1, num2)
    multi = calculator_1.mul(num1, num2)
    div = calculator_1.div(num1, num2)

    if dat == 3:
        op = sys.argv[2]
        if op == "+":
            print("{} + {} = {}".format(num1, num2, suma))
            exit(0)
        elif op == "-":
            print("{} - {} = {}".format(num1, num2, resta))
            exit(0)
        elif op == "*":
            print("{} * {} = {}".format(num1, num2, multi))
            exit(0)
        elif op == "/":
            print("{} / {} = {}".format(num1, num2, div))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
