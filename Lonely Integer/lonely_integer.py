def lonelyinteger(a):
    for item in a:
        check = [e for i, e in enumerate(a) if e == item]
        if len(check) == 1:
            return check[0]
