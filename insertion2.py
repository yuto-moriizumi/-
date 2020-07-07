array = [116, 176382, 94, 325, 3476, 4, 2542, 9, 21, 56, 322, 322]

print(array)

for i in range(1, len(array)):
    v = array[i]
    ind = i - 1
    while ind >= 0 and array[ind] > v:
        array[ind + 1] = array[ind]
        ind -= 1
    array[ind+1] = v

print(array)
