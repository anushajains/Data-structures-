from typing import TextIO

import sys

sys.setrecursionlimit(100000)
from runtime_metric import runtime_metric

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def natural_merge_sort(head):
    """
    Sorts the given linked list using natural merge sort algorithm.
    Returns the sorted linked list, number of comparisons, and number of swaps.
    """
    if head is None or head.next is None:
        return head, 0, 0

    sorted_starts = find_sorted_starts(head)
    sorted_list, comparisons, swaps = merge_sorted_sublists(sorted_starts)
    return sorted_list, comparisons, swaps


def find_sorted_starts(head):
    """
    Finds the starting nodes of sorted sublists in the linked list.
    Returns a list of the starting nodes.
    """
    sorted_starts = []
    current = head

    while current:
        start = current

        while current.next and current.next.data >= current.data:
            current = current.next

        next_node = current.next
        current.next = None
        current = next_node

        sorted_starts.append(start)

    return sorted_starts


def merge_sorted_sublists(sorted_starts):
    """
    Merges the sorted sublists into larger sorted sublists until only one sorted list remains.
    Returns the merged sorted list, number of comparisons, and number of swaps.
    """
    if not sorted_starts:
        return None, 0, 0

    if len(sorted_starts) == 1:
        return sorted_starts[0], 0, 0

    merged_starts = []
    comparisons = 0
    swaps = 0
    i = 0
    while i < len(sorted_starts):
        if i < len(sorted_starts) - 1:
            merged, comp, swp = merge(sorted_starts[i], sorted_starts[i + 1])
            merged_starts.append(merged)
            comparisons += comp
            swaps += swp
            i += 2
        else:
            merged_starts.append(sorted_starts[i])
            i += 1

    merged_list, comp, swp = merge_sorted_sublists(merged_starts)
    comparisons += comp
    swaps += swp
    return merged_list, comparisons, swaps


def merge(left, right):
    """
    Merges two sorted linked lists into a single sorted linked list.
    Returns the merged linked list, number of comparisons, and number of swaps.
    """
    if left is None:
        return right, 0, 0

    if right is None:
        return left, 0, 0

    comparisons = 0
    swaps = 0

    if left.data <= right.data:
        merged, comp, swp = left, 0, 0
        merged.next, comp, swp = merge(left.next, right)
        comparisons = comp + 1
        swaps = swp
    else:
        merged, comp, swp = right, 0, 0
        merged.next, comp, swp = merge(left, right.next)
        comparisons = comp + 1
        swaps = swp + 1

    return merged, comparisons, swaps


def print_list(head):
    """
    Prints the elements of the linked list.
    """
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


# Example usage
head = Node(1)
head.next = Node(5)
head.next.next = Node(4)
head.next.next.next = Node(6)
head.next.next.next.next = Node(7)

sorted_list, comparisons, exchanges = natural_merge_sort(head)

print("Sorted list:")
print_list(sorted_list)
print("Comparisons:", comparisons)
print("Exchanges:", exchanges)

@runtime_metric
def function5(input_file: TextIO, output_file: TextIO) -> None:
    #read input data
    data = []
    for line in input_file:
        try:
            value = int(line.strip())
            data.append(value)
        except ValueError:
            pass

    head = None
    for value in data:
        if head is None:
            head = Node(value)
            current = head
        else:
            current.next = Node(value)
            current = current.next

    sorted_head, comparisons, exchanges = natural_merge_sort(head)
    data_size = len(data)

    if data_size <= 50:
        #writes sorted list if file size is 50 or less
        current = sorted_head
        element_count = 0
        while current and element_count < 50:
            output_file.write(str(current.data) + "\n")
            current = current.next
            element_count += 1

    output_file.write(f"Using mergesort for sorting" +  "\n")
    output_file.write("Number of comparisons: " + str(comparisons) + "\n")
    output_file.write("Number of exchanges: " + str(exchanges) + "\n")
    output_file.flush()














