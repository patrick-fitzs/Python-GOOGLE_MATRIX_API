def factorial(n):
    if n == 1:
        return 1
    else:
        # call stack until n = 1, then unwind, (n1)1*n,(n2)1*n,(n3)3*n
        # so return 1*n2=n2 / 2*n3=n6 / 6*n4 = n24 / 24 *5n = 120
        return n * factorial(n-1)

print(factorial(5))