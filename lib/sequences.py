#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return

    if length == 1:
        print([0])
        return
    #initialize my_fibonacci
    my_fibonacci = [0,1] 

    #loop through my_fibonacci
    while len(my_fibonacci) < length:
      my_fibonacci.append(my_fibonacci[-2] + my_fibonacci[-1])

    print(my_fibonacci)

print(print_fibonacci(10))