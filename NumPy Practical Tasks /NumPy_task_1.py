import numpy as np


def print_array(array, message=""):
    if message:
        print(message)
    print(array)


def main():
    # Array Creation
    array = np.arange(1, 11)
    matrix = np.arange(1, 10).reshape(3, 3)

    # Indexing and Slicing
    print_array(array[2], "Access and print the third element of the one-dimensional array:")
    print_array(matrix[:2, :2], "Slice and print the first two rows and columns of the two-dimensional array:")

    # Basic Arithmetic
    print_array(array + 5, "Add 5 to each element of the one-dimensional array and print the result:")
    print_array(matrix * 2, "Multiply each element of the two-dimensional array by 2 and print the result:")


if __name__ == "__main__":
    main()
