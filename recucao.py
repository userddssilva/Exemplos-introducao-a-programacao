# fibonacci: 1, 1, 2, 3, 5, 8, 13, ...

"""
                           fib(5)
                        /          \
                     fib(4)        fib(3)
                    /    \         /   \
                 fib(2) fib(3)  fib(1) fib(2)
                /       /    \      \      \
            fib(1)    fib(1) fib(2)  1     fib(1)
            /          /        \           /
            1         1       fib(1)       1 
                               /
                              1
"""

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        

if __name__ == "__main__" :
    print(fibonacci(5))