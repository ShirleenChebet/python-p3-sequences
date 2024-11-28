#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # Print an empty list if the length is 0 or less
        return
    elif length == 1:
        print([0])  # Print [0] when the length is 1
        return
    
    fibonacci = [0, 1]
    for _ in range(2, length):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci)  # Print the list of Fibonacci numbers

if __name__ == "__main__":
    print_fibonacci(9)
