num = int(input())
def f(n):
    if n < 0:
        return False
    i = 0
    while i **2 <= n:
        if i**2 == n:
            return True
        i += 1
    return False
print((f(num)))