def maximizingXor(l, r):
    return max([a^b for a in range(l, r+1) for b in range(a, r+1)])
