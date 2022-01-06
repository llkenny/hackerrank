def catAndMouse(x, y, z):
    xz = abs(x-z)
    yz = abs(y-z)
    msg = "Mouse C"
    if xz<yz:
        msg = "Cat A"
    elif xz>yz:
        msg = "Cat B"
    return msg
