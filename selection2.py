array = [116, 176382, 94, 325, 3476, 4, 2542, 9, 21, 56, 322, 322]

print(array)

for i in range(len(array) - 1):
    minj = i
    for j in range(i, len(array)):
        if array[j] < array[minj]:
            minj = j
    t = array[minj]
    array[minj] = array[i]
    array[i] = t

print(array)
