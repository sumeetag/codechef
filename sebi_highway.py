t = int(raw_input())

for i in xrange(t):
    s, sg, fg, d, time = map(int, raw_input().strip().split(" "))
    final = ((36.0 * d * 50.0) / (10.0 * time))
    tf = s + final

    if abs(tf - sg) > abs(tf - fg):
        print "FATHER"
    elif abs(tf - sg) < abs(tf - fg):
        print "SEBI"
    else:
        print "DRAW"