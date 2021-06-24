def cho(n, m):
    c = 0

    if(n == 1 or m == 1):
        c = m+n-2
    else:
        mx = n if n > m else m
        mn = m if n > m else n
        c = cho(mn//2, mx)+cho(mn//2+mn % 2, mx)+1

    return c


d = input().split()
a = int(d[0])
b = int(d[1])

print(cho(a, b))
