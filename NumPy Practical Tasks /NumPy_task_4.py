import numpy as np


def create_array(size):
    np.random.seed(0)  # For reproducibility
    return np.random.randint(1, 42, size=size)


def save_array(array, filename):
    np.savetxt(f"{filename}.txt", array, fmt='%d')
    np.savetxt(f"{filename}.csv", array, delimiter=",", fmt='%d')
    np.save(f"{filename}.npy", array)


def load_array(filename):
    array_txt = np.loadtxt(f"{filename}.txt", dtype=int)
    array_csv = np.loadtxt(f"{filename}.csv", delimiter=",", dtype=int)
    array_npy = np.load(f"{filename}.npy")
    return array_txt, array_csv, array_npy


def sum(array, axis=None):
    return np.sum(array, axis=axis)


def mean(array, axis=None):
    return np.mean(array, axis=axis)


def median(array, axis=None):
    return np.median(array, axis=axis)


def std(array, axis=None):
    return np.std(array, axis=axis)


def print_array(array, message=""):
    if message:
        print(message)
    print(array)


def main():
    array = create_array((10, 10))
    print_array(array, "Create array:")
    save_array(array, "array")

    loaded_txt, loaded_csv, loaded_npy = load_array("array")
    print_array(loaded_txt, "Loaded Array from TXT file:")
    print_array(loaded_csv, "Loaded Array from CSV file:")
    print_array(loaded_npy, "Loaded Array from NPY file:")

    print_array(sum(array), "Total Sum:")

    print_array(mean(array), "Mean:")

    print_array(median(array), "Median:")

    print_array(std(array), "STD:")

    print_array(sum(array, axis=1), "Sum by Rows:")

    print_array(mean(array, axis=0), "Mean by Columns:")

    print_array(median(array, axis=1), "Median by Rows:")

    print_array(std(array, axis=0), "STD by Columns:")


if __name__ == "__main__":
    main()
