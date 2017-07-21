w, b = map(float, raw_input().strip().split(" "))

if (w+0.50) > b or w%5 != 0:
    print b

else:
    print format((b - 0.50 - w), '.2f')