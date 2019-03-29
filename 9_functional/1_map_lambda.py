cube = lambda x: x ** 3  # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    # fibonacii series: first two: 0 and 1
    # from the third == sum of the previous two elements
    # for eg, fib = [0 1 1 2 3] => fib[2] == fib[0] + fib[1]
    #           fib[3] = fib[2] + fib[1] etc.

    # # # # # # # # # # # #
    #  solution a
    if n == 1:
        return [0] 
    if n == 0:
        return [] 
    # from the explanation above: we need [0, 1] to get started,
    fib = [0,1]
    # for loop from the third element, till the end of list 
    for i in range(2,n):
        # fib += sum(fib[i-2:i-1])
        fib += [sum(fib[i-2:i])]
    return fib

    # # # # # # # # # # # #
    #  solution b
    fib = [0,1] 
    for i in range(2,n): 
        fib += [sum(fib[i-2:i])]
    return fib[0:n]
    
    # return [sum(fib[i-2,i-1]) for x in range(n)]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
