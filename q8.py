rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of Matrix:")
matrix= [[int(input()) for i in range(column)] for i in range(rows)]
print("-------Your  Matrix is---------")
for n in matrix:
    print(n)

#result matrix of column*row  dimension

result =[[0 for i in range(rows)] for j in range(column)]

#transpose the matrix
for r in range(rows):
   
   for c in range(column):
       #here we are grabbing the row data of matrix and putting it in the column on the result
       result[c][r] = matrix[r][c]

print("Transpose matrix is: ")
for r in result:
    print(r)