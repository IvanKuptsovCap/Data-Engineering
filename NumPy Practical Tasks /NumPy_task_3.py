import numpy as np


def create_array(size):
    np.random.seed(0)
    return np.random.randint(1, 42, size=size)


def transpose(data):
    return data.T


def reshape(data, shape):
    return data.reshape(shape)


def split(data, num_splits, axis=0):
    return np.array_split(data, num_splits, axis=axis)


def combine(*arrays, axis=0):
    return np.concatenate(arrays, axis=axis)


def print_array(array, message=""):
    if message:
        print(message)
    print(array)


def main():
    # Array Creation
    initial_array = create_array((6, 6))
    print_array(initial_array, "Creation 6x6 Array:")

    # Transpose array
    print_array(transpose(initial_array), "Transposed Array:")

    # Reshape array
    print_array(reshape(initial_array, (3, 12)), "Reshaped Array:")

    # Split array
    split_arrays = split(initial_array, 3, axis=0)
    for i, sub_array in enumerate(split_arrays):
        print_array(sub_array, f"Sub-array {i + 1}:")

    # Combine sub-arrays
    combined_array = combine(*split_arrays, axis=0)
    print_array(combined_array, "Combined Array:")


if __name__ == "__main__":
    main()
