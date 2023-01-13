#!/usr/bin/python3
"""
Module: 5-text_indentation
Content: program that edits text by adding 2 newlines
after (.), (?) and (:).
"""

def text_indentation(text):
    for i in range(len(text)):
        if text[i] == "." or text[i] == ":" or text[i] == "?":
            print(text[i])
            print()
            i += 2
        else:
            if (text[i] == " " and (text[i - 1] == "." or
                                    text[i - 1] == ":" or
                                    text[i - 1] == "?")):
                continue
            print(text[i], end="")
