def search_in_matrix(matrix, target):
    return [(x, y) for x in range(len(matrix)) for y in range(len(matrix[x])) if matrix[x][y] == target][0]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]
target = 44

try:
    print(search_in_matrix(matrix, 44))
except Exception as IndexError:
    print((-1, -1))