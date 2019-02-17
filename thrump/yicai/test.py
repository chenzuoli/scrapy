#!/bin/python
str="abc.1234"
split=str.split(".", 2)
print split
if split[1].isdigit():
    print split[1]
