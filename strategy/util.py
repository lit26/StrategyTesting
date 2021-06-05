def cross(ind1, ind2):
    above = (ind1 > ind2).astype(int)
    buySell = above.diff()
    return buySell
