n, m, r = 4, 4, 2

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

mat = []
layers = min(n, m) // 2

for layer in range(layers):
    temp = []
    # first row elements (without last)
    for i in range(layer, n - 1 - layer):
        temp.append(matrix[layer][i])
    # print(temp)

    # last column elements (without last)
    for i in range(layer, m - 1 - layer):
        temp.append(matrix[i][n - 1 - layer])
    # print(temp)

    # last row elements (backwards, without first)
    for i in range(n - 1 - layer, layer, -1):
        temp.append(matrix[m - 1 - layer][i])
    # print(temp)

    # first column elements (backwards, without first and last)
    for i in range(m - 1 - layer, layer, -1):
        temp.append(matrix[i][layer])
    print(temp)
    mat.append(temp)

for layer in range(layers):
    row = mat[layer]

    index = r % len(row)


    def increment_index():
        global index
        index = (index + 1) % len(row)
        return index

    # first row elements (without last)
    for i in range(layer, n - 1 - layer):
        matrix[layer][i] = row[index]
        index = increment_index()
    # print(temp)

    # last column elements (without last)
    for i in range(layer, m - 1 - layer):
        matrix[i][n - 1 - layer]= row[index]
        index = increment_index()
    # print(temp)

    # last row elements (backwards, without first)
    for i in range(n - 1 - layer, layer, -1):
        matrix[m - 1 - layer][i]= row[index]
        index = increment_index()
    # print(temp)

    # first column elements (backwards, without first and last)
    for i in range(m - 1 - layer, layer, -1):
        matrix[i][layer]= row[index]
        index =increment_index()

for row in matrix:
    print(*row)