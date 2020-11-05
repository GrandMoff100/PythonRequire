def myfunc(x, target=30, index=0):
    if len(x) < target:
        x += x[index]
    elif len(x) > target:
        x = x[:-2]
    else:
        return x
    return myfunc(x, target, index + 1)
