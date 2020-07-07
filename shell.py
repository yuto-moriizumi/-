array = [116, 176382, 94, 325, 3476, 4, 2542, 9, 21, 56, 322, 322]

print(array)


def insertion(array, g):
    for i in range(g, len(array)):
        v = array[i]
        j = i-g
        while j >= 0 and array[j] > v:
            array[j + g] = array[j]
            j = j - g
        array[j+g] = v


def shellsort(array):
    G = [1, 4, 13, 40, 121]
    for i in G[::-1]:
        insertion(array, i)


shellsort(array)
print(array)
