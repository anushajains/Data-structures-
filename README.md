# Quicksort and Merge sort 
-Anusha Jain
The programs compare the performance of two sorting algorithms: Quicksort and Natural Merge Sort. I implemented four versions of Quicksort with different pivot selection methods and stopping cases, and also implemented Natural Merge Sort using a linked implementation. 
This document is written in [Markdown](https://dillinger.io/)
run with python 3.10

### Project Layout

* [AnushaJLab4](.): The parent or "root" folder containing all of these files. 
    * [README.md](README.md): explains the project
    * AnushaJANALYSIS: Analysis of the project pdf file
* [`runtime_metric`](lab4filesAnushaJ/runtime)
     This file contains program code to check how long program takes to execute in seconds.
* [`quicksort1.py`](lab4filesAnushaJ/lab4/quicksort1.py)
    This program uses quicksort -> Selects the first item of the partition as the pivot. Treats partitions of size one and two as stopping cases.
* [`quicksort2.py`](lab4filesAnushaJ/lab4/quicksort2.py)
    This program uses quicksort -> Same pivot selection. For a partition of size 100 or less, uses an insertion sort to finish.
* [`quicksort3.py`](lab4filesAnushaJ/lab4/quicksort3.py)
    This program uses quicksort -> Same pivot selection. For a partition of size 50 or less, uses an insertion sort to finish.
* [`quicksort4.py`](lab4filesAnushaJ/lab4/quicksort4.py)
    This program uses quicksort -> Selects the median-of-three as the pivot. Treats partitions of size one and two as stopping cases
* [`merge.py`](lab4filesAnushaJ/lab4/merge4.py)
    This program uses natural merge sort  using a linked implementation.

* [`main.py`](lab4filesAnushaJ/main.py) 
        This file is the entrypoint to the program when ran as a program. 

###  quicksort1 program
* takes an array arr as input, along with optional parameters for comparisons and exchanges (initialized to 0)
* chooses the first element as pivot
* sorts the array
* returns the sorted array, comparisons exchanges
* reads input file and writes to output file

###  quicksort2 program
* takes an array arr as input, along with optional parameters for comparisons and exchanges (initialized to 0)
* chooses the first element as pivot
* sorts the array
* when the file size reaches less than 100 , performs insertion sort on the remaining elements
* returns the sorted array, comparisons exchanges
* reads input file and writes to output file
 
###  quicksort3 program
* takes an array arr as input, along with optional parameters for comparisons and exchanges (initialized to 0)
* chooses the first element as pivot
* sorts the array
* when the file size reaches less than 50 , performs insertion sort on the remaining elements
* returns the sorted array, comparisons exchanges
*  reads input file and writes to output file

###  quicksort4 program
* takes an array arr as input, along with optional parameters for comparisons and exchanges (initialized to 0)
* chooses the median of the first middle and last element as pivot
* sorts the array
* when the file size reaches less than 100 , performs insertion sort on the remaining elements
* returns the sorted array, comparisons exchanges
* reads input file and writes to output file

### merge program
* finds the starting nodes of sorted sublists in the linked list
* repeatedly merges adjacent sublists until only one sorted list remains. It uses the merge function to merge two sorted sublists
* The comparisons and swaps are counted during the merging process.
* returns the sorted array, comparisons exchanges
* reads input file and writes to output file

### Files 
input naming scheme orderofdata+size of file
* asc50: input file I created that has sorted values 
* ran50:input file I created that has randomly sorted values 
* rev50: input file I created that has decreasing sorted values
* dup1k: input file containing randomly sorted data with duplicates

output file name scheme orderofdata+sizeof file_sortingalgorithmused
* asc50out_merge: output file
* asc50out_quicksort1: output file
* asc50out_quicksort2: output file
* asc50out_quicksort3: output file
* asc50out_quicksort4: output file
* ran50out_merge: output file
* ran50out_quicksort1: output file
* ran50out_quicksort2: output file
* ran50out_quicksort3: output file
* ran50out_quicksort4: output file
* rev50out_merge: output file
* rev50out_quicksort1: output file
* rev50out_quicksort2: output file
* rev50out_quicksort3: output file
* rev50out_quicksort4: output file
* ascbig: output file that has output for ascending order input for all sorting algorithms when input file size is 1000,2000,5000 and 10000
*  ranbig: output file that has output for randomly sorted input for  all sorting algorithms when input file size is 1000,2000,5000 and 10000
*  revbig: output file that has output for descending order data for all sorting algorithms when input file size is 1000,2000,5000 and 10000
*  dup1Kout: output file that has output comparisons and exchanges for dup1k input


### Running this project 
1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. In command line open command line in the same directory as the saved python files(this project) using `cd directorypath`
4. Run the program (with real inputs): `python  main.py program_name <some_input_file> <some_output_file>` ex python main.py quicksort1 asc50.dat asc50out_quicksort1.txt
5. input files and output files are in the resources folder of the zip file in this project

### Usage
This program sorts the input files with different sorting algorithms 

##### Sample input and output text 
Sample input(for quicksort1):-
``` 
[1,2,5,4,3]
```
Sample output (for quicksort1) :-
```
[1, 2, 3, 4, 5]
comparisons: 10
exchanges: 3
```
similarly the other programs will take input and give output


      








