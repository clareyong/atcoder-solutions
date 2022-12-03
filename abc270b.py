x, y, z = map(int, input().split())
if x > 0:
    if x < y:
        print(x)
        exit()
    elif y < x:
        if y < 0:
            print(x)
            exit()
        elif z < y:
            if z > 0:
                print(x)
                exit()
            else:
                print(2 * abs(z) + x)
                exit()
        else:
            print(-1)
            exit()
if x < 0:
    if x > y:
        print(abs(x))
        exit()
    elif x < y:
        if y > 0:
            print(abs(x))
            exit()
        elif y < 0:
            if z < y:
                if z < x:
                    print(-1)
                    exit()
                elif z > x:
                    print(-1)
                    exit()
            elif z > y:
                if z < 0:
                    print(abs(x))
                    exit()
                if z > 0:
                    print(abs(x) + 2 * abs(z))
                    exit()
            else:
                print(-1)
                exit()
