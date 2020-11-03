# 1, 1, 2, 3, 5, 8, 13

fibonacci(6)

                        8 fib(6)
                    /                \ 
             5  fib(5)               3    fib(4)
             /       \                /           \
    3    fib(4)     2 fib(3)          2 fib(3)     1 fib(2)
        /  \        /     \           /    \            /
2    fib(3) 1 fib(2) 1 fib(2)   1 fib(1)  1 fib(2)    1
    /  \      \      /       /        /      \ 
2 fib(2) fib(1) 1     1       1        1     1
  /       \
  1       1
               

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
