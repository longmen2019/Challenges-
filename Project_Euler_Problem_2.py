"""
Reference https://www.youtube.com/watch?v=QNMrJ3An8eE

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
 By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms."""

# def fib(to=10):
#     a = 1
#     b = 2
    
#     for i in range(to):
#         yield a
#         # temp = a + b
#         a, b = b , a+b
#         # b = temp
#         # select the only even value numbers 
# print (sum([i for i in fib() if i % 2==0]))


def fib(max=10):
    a = 1
    b = 2
    
    while a < max:
        yield a
        # temp = a + b
        a, b = b , a+b
        # b = temp
        # select the only even value numbers 
print (sum([i for i in fib(10000000) if i % 2==0]))

