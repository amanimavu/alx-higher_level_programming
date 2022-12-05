#!/usr/bin/python3

# Print a matrix of integers
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
	return None
    else:
        for row in matrix:
            for col in range(0, len(row)):
                if col == len(row) - 1:
                    print("{}".format(row[col]))
                else:
                    print("{} ".format(row[col]), end="")
