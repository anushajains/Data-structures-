# Huffman Encoding Tree 
-Anusha Jain
The program implements Huffman Encoding, a lossless data compression algorithm. The implementation focuses on building a Huffman Encoding Tree from a frequency table. It includes a function that generates the encoding for each character and a function that decodes encoded text to alphabets.
This document is written in [Markdown](https://dillinger.io/)
run with python 3.10


###  build_huffman_tree() function 
* takes a frequency table as input  
* creates a priority queue of nodes, sorted by frequency
* repeatedly merges the two nodes with the lowest frequency until there is only one node left
* root node of the Huffman Encoding Tree is returned 


### generate_encoding() function
 * Takes the root node of the Huffman Encoding Tree as input 
 * Traverses the tree to generate the Huffman encoding for each character in the tree
 * Assigns a "0" to each left edge and a "1" to each right edge 
 * At leaf node, it adds the character and its corresponding encoding to a list of encodings.
 * Returns a list of tuples, which is the Huffman encoding
 
### decode_text function
* takes a binary string 
* uses the same Huffman tree 
* Traverses down tree and finds character
*  decodes the binary string back into the original text
* Returns decoded text

### encode_text function
* Takes a string of text as input
* Calls the build_huffman_tree function to construct a Huffman tree using 
* calls the generate_encoding function to generate encodings for each character in the Huffman tree.
* initializes an empty string called encoded_text.
* It loops through each character in the input text, converting each character to uppercase
* For each character, it checks whether it is a newline character (\n)
* If it is not a newline character, it searches for the encoding for that character in the encodings. 
* Appends the corresponding code to the encoded_text string. 
* Returns encoded text

### preorder_traversal function
* prints preorder tree to the output console
* Checks if node is leaf not or not and accordingly prints the tree

### Process_files function
* reads frequency table, builds Huffman tree and generates encodings
* writes to output file
* Checks if input file contents are number or letters, proceeds to call function to decode or encode them respectively.
* Writes to output file

### Files
* ClearText.txt : Given required input file containing alphabets 
* FreqTable.txt: Given required input file containing the frequency table
* Encoded.txt: Given required input file containing digits
* cleartext_ex1: Student generated test input containing alphabets and encoded using FreqTable.txt
* cleartext_ex2: Student generated test input containing alphabets and encoded using FreqTable_ex2.txt
* encoded_ex1:  Student generated test input containing digits and decoded using FreqTable.txt
* encoded_ex2
* FreqTable_ex2:  Student generated test input containing alphabets and decoded using FreqTable_ex2.txt
* Output_FreqTable_ClearText_Encoded: Output file for the input of ClearText.txt, FreqTable.txt and Encoded.txt
* Output_FreqTable_cleartextex1_encodedex1: Output file for FreqTable.txt, cleartext_ex1.txt and encoded_ex1.txt
* Output_FreqTable_ex2_cleartextex2_encodedex2: Output file for FreqTable_ex2.txt, cleartext_ex2.txt and encoded_ex2.txt

### Running this project 
1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. In command line open command line in the same directory as the saved python files(this project) using `cd directorypath`
4. since the file takes three input files and writes to one output file in the command line be sure to input the frequency file as the first input file to obtain output
5. Run the program (with real inputs): `python  main.py <some_input_file> <some_input_file> <some_input_file> <some_output_file>`
6. input files and output files are in the resources folder of the zip file in this project

### Usage
This program reads Frequency table from the input file and proceeds to build Huffman tree. Encodings are generated for all leaf node characters which are used to decode and encode input from two other files.

##### Sample input and output text 
Sample input:-
``` 
character   Frequency
    a            5
    b           9
    c           12
    d           13
    e           16
    f           45
    
   decode: 1001011101
   encode: abd
```
Sample output :-
```
f: 0
c: 100
d: 101
a: 1100
b: 1101
e: 111

cdb
11001101101
```

### Project Layout

* [AnushaJLab3](.): The parent or "root" folder containing all of these files. 
    * [README.md](README.md): explains the project
    *AnushaJANALYSIS: Analysis of the project pdf file
     * [`runtime_metric`](lab3filesAnushaJ/runtime)
     This file contains program code to check how long program takes to execute in seconds.
     * [`lab3.py`](lab3filesAnushaJ/lab3.py)
     This file contains the program utilizing stack.
      * [`main.py`](lab3filesAnushaJ/main.py) 
        This file is the entrypoint to the program when ran as a program. 
      







