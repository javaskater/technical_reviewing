#!/usr/bin/python3

filename="myfile1.txt"
try:
    f =  open(filename, 'r')
    for line in f:
        print(line)
except Exception as e:
    raise e
finally:
    f.close()