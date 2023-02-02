# declaring the number of rows
no_of_rows = 5

# First for loop to print the first 5 columns of the pattern in increasing order
for i in range(0, no_of_rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
