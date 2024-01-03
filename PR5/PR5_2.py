rows = 7
cols = 7
array = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        array[i][j] = 7 - i

for row in array:
    print(' '.join(map(str, row)))
