from typing import TextIO
from runtime_metric import runtime_metric

def quicksort_median_of_three(arr, comparisons=0, swaps=0):
    """
    Sorts the given array using quicksort with the median of three pivot selection strategy.
    Returns the sorted array, number of comparisons, and number of swaps.
    """
    comparisons = 0

    # Base cases
    if len(arr) <= 1:
        return arr, comparisons, swaps
    elif len(arr) == 2:
        comparisons += 1
        if arr[0] > arr[1]:
            swaps += 1
            arr[0], arr[1] = arr[1], arr[0]
        return arr, comparisons, swaps
    else:
        # Choose the pivot using the median of three strategy
        first = arr[0]
        last = arr[-1]
        middle = arr[len(arr) // 2]
        pivot_candidates = sorted([first, middle, last])
        pivot = pivot_candidates[1]
        pivot_duplicates = [x for x in arr if x == pivot]

        left = []
        right = []
        left_indices = []  # Track indices of elements in the left partition
        right_indices = []  # Track indices of elements in the right partition

        # Partition the array based on the pivot
        for i in range(len(arr)):
            comparisons += 1
            if arr[i] == first or arr[i] == middle or arr[i] == last:
                comparisons += 1
            if arr[i] < pivot:
                left.append(arr[i])
                left_indices.append(i)
            elif arr[i] > pivot:
                right.append(arr[i])
                right_indices.append(i)

        # Recursively sort the left and right partitions
        sorted_left, left_comparisons, left_swaps = quicksort_median_of_three(left, comparisons, swaps)
        sorted_right, right_comparisons, right_swaps = quicksort_median_of_three(right, comparisons, swaps)

        # Merge the sorted partitions along with the pivot duplicates
        result = sorted_left + pivot_duplicates + sorted_right
        comparisons += left_comparisons + right_comparisons

        # Calculate swaps in memory
        in_memory_swaps = 0
        for i, index in enumerate(left_indices):
            if index != i + swaps:
                in_memory_swaps += 1
        for i, index in enumerate(right_indices):
            if index != i + swaps + len(left) + 1:
                in_memory_swaps += 1

        # Calculate total swaps (array swaps + swaps in memory)
        total_swaps = swaps + left_swaps + right_swaps + in_memory_swaps

        return result, comparisons, total_swaps


arr = [1, 2, 5, 4, 3]
sorted_arr, comparisons, swaps = quicksort_median_of_three(arr)

print(sorted_arr)
print(comparisons)
print(swaps)

@runtime_metric
def function4(input_file: TextIO, output_file: TextIO) -> None:
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

    sorted_data, comparisons, exchanges = quicksort_median_of_three(data)

    # write sorted data, comparisons, and exchanges to output file

    if len(sorted_data) <= 50:
        output_file.write(f"Sorted data: {sorted_data}\n")
        output_file.write(f"Number of comparisons: {comparisons}\n")
        output_file.write(f"Number of exchanges: {exchanges}\n")
    else:
        output_file.write(f"Using quicksort4 for sorting  \n")
        output_file.write(f"Number of comparisons: {comparisons}\n")
        output_file.write(f"Number of exchanges: {exchanges}\n\n")
    output_file.flush()



