array = [116, 176382, 94, 325, 3476, 4, 2542, 9, 21, 56, 322, 322]

print(array)

SENTINEL = 10**12


def merge(array, left, mid, right):
    L = array[left:mid]
    R = array[mid:right]
    L.append(SENTINEL)
    R.append(SENTINEL)
    i = j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1


def mergeSort(array, left, right):
    if (left + 1 < right):
        mid = (left + right) // 2
        mergeSort(array, left, mid)
        mergeSort(array, mid, right)
        merge(array, left, mid, right)


mergeSort(array, 0, len(array))
print(array)
