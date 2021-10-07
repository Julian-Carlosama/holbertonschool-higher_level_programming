#!/usr/bin/python3
"""
function that prints
a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    must be a string,
    raise a TypeError
    exception with the message text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == ".":
            print(".\n")
        elif text[i] == "?":
            print('?\n')
        elif text[i] == ":":
            print(":\n")
        else:
            if (text[i] == " " and (text[i - 1]
                                    in ".?:" or text[i - 1] == " ")):
                continue
            print("{}".format(text[i]), end="")
