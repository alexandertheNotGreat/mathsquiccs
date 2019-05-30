def sqrt(num):
    '''
    square root of (x)
    (EX: sqrt(6) == 720)
    '''
    s = num * num
    return s
def gett(*num):
    '''
    some (infinite) numbers to add
    Ex: gett(10, 6, 4, 8, 0, 1) == 29
    '''
    s = sum(num)
    return s
def times(num, n):
    '''
    mutiplies (two) numbers
    ex: times(2, 1) == 2
    '''
    s = num * n
    return s
def divide(n, num):
    '''
    divide numbers
    ex: divide(10, 2) == 5 (yeah i'm dumb).
    '''
    s = n / num
    return s
def fat(n=1):
    '''
    factorial of a number.
    Example: fat(1) ==  0, 1, 1, 2, 3, 5...
    '''
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f