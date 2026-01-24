import numpy as np
""" With NumPy, you can perform a wide range of numerical operations, including:
Creating and manipulating arrays.
Performing element-wise and matrix operations.
Generating random numbers and statistical calculations.
Conducting linear algebra operations.
Working with Fourier transformations.
Handling missing values efficiently in datasets."""


def create_array(data, dtype=None):
    """Create a NumPy array from the given data with optional data type."""
    return np.array(data, dtype=dtype)

def array_operations():
    """Demonstrate basic NumPy array operations."""
    arr1 = create_array([1, 2, 3, 4, 5])
    arr2 = create_array([[1, 2], [3, 4]], dtype=float)
    print("Array 1:", arr1)
    print("Array 2:", arr2)

    # Basic operations
    print("Sum of Array 1:", np.sum(arr1))
    print("Mean of Array 2:", np.mean(arr2))

    # Reshaping
    reshaped = arr1.reshape((5, 1))
    print("Reshaped Array 1:\n", reshaped)

    # Element-wise operations
    arr3 = create_array([10, 20, 30, 40, 50])
    print("Element-wise addition:", arr1 + arr3)
    print("Element-wise multiplication:", arr1 * arr3)

    # Slicing
    print("Sliced Array 1:", arr1[1:4])

    # Broadcasting
    broadcasted = arr1 + 10
    print("Broadcasted Array 1:", broadcasted)

    # Transpose
    transposed = arr2.T
    print("Transposed Array 2:\n", transposed)

    # Flatten       
    flattened = arr2.flatten()
    print("Flattened Array 2:", flattened)

    # Random array
    random_arr = np.random.rand(3, 2)
    print("Random Array:\n", random_arr)

    # Concatenation
    concatenated = np.concatenate((arr1.reshape((5, 1)), arr1.reshape((5, 1))), axis=1)
    print("Concatenated Array:\n", concatenated)

    # Sorting
    sorted_arr = np.sort(arr1)
    print("Sorted Array 1:", sorted_arr)

    # Unique elements
    unique_elements = np.unique(create_array([1, 2, 2, 3, 4, 4, 5]))
    print("Unique elements in Array 1:", unique_elements)

    # Set operations
    arr4 = create_array([3, 4, 5, 6, 7])
    intersection = np.intersect1d(arr1, arr4)
    print("Intersection of Array 1 and 4:", intersection)
    union = np.union1d(arr1, arr4)
    print("Union of Array 1 and 4:", union)
    difference = np.setdiff1d(arr1, arr4)
    print("Difference of Array 1 and 4:", difference)

    # Indexing
    indexed = arr1[2]
    print("Indexed Array 1:", indexed)

    # Advanced indexing
    advanced_indexed = arr1[[0, 2, 4]]
    print("Advanced Indexed Array 1:", advanced_indexed)

    # Filtering
    filtered = arr1[arr1 > 3]
    print("Filtered Array 1:", filtered)

    # Stacking
    stacked = np.vstack((arr1, arr3))
    print("Stacked Arrays:\n", stacked)

    # Resizing
    resized = np.resize(arr1, (3, 2))
    print("Resized Array 1:\n", resized)

    # Adding and removing elements
    appended = np.append(arr1, [6, 7, 8])
    print("Appended Array 1:", appended)
    removed = np.delete(arr1, [0, 2])
    print("Removed Array 1:", removed)

    # Splitting
    split_arr = np.array_split(arr1, 2)
    print("Split Array 1:", split_arr)

    # Save and load
    np.save('array1.npy', arr1)
    loaded_arr = np.load('array1.npy')
    print("Loaded Array from file:", loaded_arr)

# Run the demonstration
if __name__ == "__main__":
    array_operations()