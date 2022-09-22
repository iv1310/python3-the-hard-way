"""
Suppose I want to flatten a given 2-D list:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Expected Output: flatten_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flatten_matrix = []

# Using classic approach
for i in matrix:
    for x in i:
        flatten_matrix.append(x)

print(flatten_matrix)

# Using list comprehension
flaaten_matrix = [i for x in matrix for i in x]
"""
it will be the same with
flaaten_matrix = [val
            for x in matrix
            for val in x
]
"""
print(flaaten_matrix)
