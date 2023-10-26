from typing import List, Tuple, TextIO
import sys

sys.setrecursionlimit(10000)
from runtime_metric import runtime_metric
def quicksort_first_pivot_insertion_sort(arr: List[int], comparisons: int = 0, exchanges: int = 0) -> Tuple[List[int], int, int]:
    """
    Sorts the given array using quicksort with the first element as the pivot.
    If the length of the array is less than or equal to 50, uses insertion sort.
    Returns the sorted array, number of comparisons, and number of exchanges.
    """
    comparisons = 0

    # Base cases
    if len(arr) <= 1:
        return arr, comparisons, exchanges
    elif len(arr) == 2:
        comparisons += 1
        if arr[0] > arr[1]:
            exchanges += 1
            arr[0], arr[1] = arr[1], arr[0]
        return arr, comparisons, exchanges
    elif len(arr) <= 50:
        return insertion_sort(arr, comparisons, exchanges)
    else:
        pivot = arr[0]
        left = []
        right = []
        left_indices = []  # Track indices of elements in the left partition
        right_indices = []  # Track indices of elements in the right partition

        # Partition the array based on the pivot
        for i in range(1, len(arr)):
            comparisons += 1
            if arr[i] <= pivot:
                left.append(arr[i])
                left_indices.append(i)
            else:
                right.append(arr[i])
                right_indices.append(i)

        # Recursively sort the left and right partitions
        sorted_left, left_comparisons, left_exchanges = quicksort_first_pivot_insertion_sort(left, comparisons, exchanges)
        sorted_right, right_comparisons, right_exchanges = quicksort_first_pivot_insertion_sort(right, comparisons, exchanges)

        # Merge the sorted partitions
        result = sorted_left + [pivot] + sorted_right
        comparisons += left_comparisons + right_comparisons

        in_memory_swaps = 0
        # Count swaps in memory
        for i, index in enumerate(left_indices):
            if index != i + exchanges:
                in_memory_swaps += 1
        for i, index in enumerate(right_indices):
            if index != i + exchanges + len(left) + 1:
                in_memory_swaps += 1

        exchanges += left_exchanges + right_exchanges + in_memory_swaps

        return result, comparisons, exchanges


def insertion_sort(arr: List[int], comparisons: int = 0, exchanges: int = 0) -> Tuple[List[int], int, int]:
    """
    Sorts the given array using insertion sort.
    Returns the sorted array, number of comparisons, and number of exchanges.
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            comparisons += 1
            exchanges += 1
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        comparisons += 1

    return arr, comparisons, exchanges

arr = [1,2,3]
sorted_arr, comparisons, exchanges = quicksort_first_pivot_insertion_sort(arr)


print(sorted_arr)
print(comparisons)
print(exchanges)

@runtime_metric
def function3(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads integers from an input file and sorts them using quicksort with the first element as the pivot.
    The final number of comparisons and exchanges, as well as the sorted data, are written to the output file.
    :param input_file: An opened text file set to read mode
    :param output_file: An opened text file set to write mode
    """
    # read input data

    data = []
    for line in input_file:
        try:
            data.append(int(line))
        except ValueError:
            pass

    # sort data using quicksort and count comparisons and exchanges
    sorted_data, comparisons, exchanges = quicksort_first_pivot_insertion_sort(data)

    # write sorted data, comparisons, and exchanges to output file
    if len(sorted_data) <= 50:
        output_file.write(f"Sorted data: {sorted_data}\n")
        output_file.write(f"Number of comparisons: {comparisons}\n")
        output_file.write(f"Number of exchanges: {exchanges}\n")
    else:
        output_file.write(f"Using quicksort3 for sorting  \n")
        output_file.write(f"Number of comparisons: {comparisons}\n")
        output_file.write(f"Number of exchanges: {exchanges}\n\n")
    output_file.flush()
