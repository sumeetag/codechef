t = int(raw_input())
for i in xrange(t):
    n = raw_input().strip()
    if len(n.split(" ")) == 1:
        print n.title()

    else:
        n = n.title()
        l = n.split(" ")
        s = ""
        for j in xrange(len(l)-1):
            s += l[j][0] + ". "
        s+= l[-1]
        print s




