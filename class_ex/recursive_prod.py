def prod_range(start, end):
    if start == end:
        return start
    return start * prod_range(start+1, end)


print(prod_range(2,7))