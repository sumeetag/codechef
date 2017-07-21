import fractions

def lcm(x, y):
    """This function takes two
    integers and returns the L.C.M."""

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

def lcm2(a, b):
    return a * b / fractions.gcd(a, b)


t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    l = map(int, raw_input().strip().split(" "))
    mm = 100000000
    for j in xrange(len(l)-1):
        for k in xrange(j+1, len(l)):
            m = lcm2(l[j], l[k])
            if m < mm:
                mm = m
    print mm
