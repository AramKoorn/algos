def meet():
    return

l = ...
r = ...

while l < r:
    m = (l + r) // 2
    # print(m)
    if meet():
        r = m
    else:
        l = m + 1

print(l)


