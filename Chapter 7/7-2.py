#202311388 김민상
def fib_dp_tab(n) :
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1) :
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = int(input("피보나치수의 n번째 자리 : "))
print(fib_dp_tab(n))