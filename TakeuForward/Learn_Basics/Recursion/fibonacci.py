
# while True:
#     a = 0
#     b = 1
#     n = int(input("Nth fibonacci : "))
#     for i in range(1,n):
#         sum = a+b
#         a = b
#         b = sum

#     print(a)



def fibonac(n):
    if n<=1:
        return n
    
    last = fibonac(n-1)
    slast = fibonac(n-2)

    return (last + slast)
     


def fib(n: int,memo=None) -> int:
    if memo is None:
        memo={}
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]


print(fibonac(40))
# print(fib(40))