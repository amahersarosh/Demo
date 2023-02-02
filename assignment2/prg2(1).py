# declaring the number of rows
no_of_rows = 5
# Second for loop to print the second half of the pattern in decreasing order
for i in range(no_of_rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
print("\r")
