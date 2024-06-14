#!/usr/bin/python3

filename="myfile1.txt"
with open(filename, 'r') as f:
    for line in f:
        print(line)