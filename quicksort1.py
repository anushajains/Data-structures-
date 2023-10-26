from typing import TextIO
from runtime_metric import runtime_metric

def quicksort_first_pivot_verbose(arr, comparisons=0, exchanges=0):
    """
    Sorts the given array using the first element as the pivot.
    Returns the sorted array, number of comparisons, and number of exchanges.
    """
    comparisons=0
   #base cases
    if len(arr) <= 1:
        return arr, comparisons, exchanges
    elif len(arr) == 2:
        comparisons += 1
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            exchanges += 1

        return arr, comparisons, exchanges
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
        sorted_left, left_comparisons, left_exchanges = quicksort_first_pivot_verbose(left, comparisons, exchanges)
        sorted_right, right_comparisons, right_exchanges = quicksort_first_pivot_verbose(right, comparisons, exchanges)
        # Merge the sorted partitions
        result = sorted_left + [pivot] + sorted_right
        comparisons += left_comparisons + right_comparisons


      #count swaps in memory
        in_memory_swaps = 0
        for i, index in enumerate(left_indices):
         if index != i + exchanges :
            in_memory_swaps += 1
        for i, index in enumerate(right_indices):
         if index != i + exchanges + len(left) + 1:
            in_memory_swaps += 1
        # Calculate total swaps (array swaps + swaps in memory)
        exchanges += left_exchanges + right_exchanges + in_memory_swaps





    return result, comparisons, exchanges



arr = [1,2,5,4,3]
sorted_arr, comps, exch = quicksort_first_pivot_verbose(arr)
print(sorted_arr)
print(comps)
print(exch)
@runtime_metric
def function1(input_file: TextIO, output_file: TextIO) -> None:
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

    sorted_data, comparisons, exchanges = quicksort_first_pivot_verbose(data)

    # write sorted data, comparisons, and exchanges to output file

    if len(sorted_data) <= 50:
        output_file.write(f"Sorted data: {sorted_data}\n")
        output_file.write(f"Number of comparisons: {comparisons}\n")
        output_file.write(f"Number of exchanges: {exchanges}\n")
    else:
        output_file.write(f"Using quicksort1 for sorting  \n")
        output_file.write(f"Number of comparisons: {comparisons}\n")
        output_file.write(f"Number of exchanges: {exchanges}\n\n")
    output_file.flush()




