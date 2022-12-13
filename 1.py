a = int(input())
k = 0
for j in range(a):
    v = int(input())
    if v == 1:
        k += 1
print(k if k < a / 2 else a - k)
