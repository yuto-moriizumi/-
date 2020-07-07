array = [116, 176382, 94, 325, 3476, 4, 2542, 9, 21, 56, 322, 322]

print(array)


def quick(array):
    if len(array) == 0:
        return array
    L = []
    R = []
    for i in array[:-1]:
        if i <= array[-1]:
            L.append(i)
        else:
            R.append(i)
    L = quick(L)
    R = quick(R)
    L.append(array[-1])
    L.extend(R)
    return L


array = quick(array)

print(array)
