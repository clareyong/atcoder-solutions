h, m = map(int, input().split())
while True:
    if h < 10 and h > 5:
        h += 10 - h
        m = 0
        print(f'{h} {m}')
        exit()
    elif h < 20 and h > 15:
        h += 20 - h
        m = 0
        print(f'{h} {m}')
        exit()
    elif m + 1 < 60:
        if len(str(m)) == 1:
            curr = str(0) + str(m)
        else:
            curr = str(m)
        if h >=20:
            if int(curr[0]) <= 3:
                print(f'{h} {m}')
                exit()
            else:
                m += 1
        elif h < 20:
            print(f'{h} {m}')
            exit()
    else:
        if h + 1 < 24:
            h += 1
            m = 0
            print(f'{h} {m}')
            exit()
        else:
            h = 0
            m = 0
            print(f'{h} {m}')
            exit()