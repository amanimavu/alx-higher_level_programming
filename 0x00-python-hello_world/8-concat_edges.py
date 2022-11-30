#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programing\
		language that combines remarkable power with very clear syntax"
str = str[str.find("object"):str.find("programing")+10] + str[str.find(" ")] + str[str.find("with"):str.find("very")]  + str[: str.find(" ")]
print(str)
