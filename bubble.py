array = [116, 176382, 94, 325, 3476, 4, 2542, 9, 21, 56, 322, 322]

print(array)

flag = 1
i = 0
while flag:
    flag = 0
    for j in range(len(array) - 1, i, -1):
        if array[j - 1] > array[j]:
            t = array[j-1]
            array[j-1] = array[j]
            array[j] = t
            flag = 1
    i += 1


print(array)
