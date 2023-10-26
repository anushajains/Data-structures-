import argparse
from pathlib import Path
import sys

# Set the recursion limit for Python to avoid stack overflow in recursive functions
sys.setrecursionlimit(100000)

from quicksort1 import function1
from quicksort2 import function2
from quicksort3 import function3
from quicksort4 import function4
from merge import function5


def main():
    # Create an argument parser
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("program", type=str, help="Name of the program to run")
    arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
    arg_parser.add_argument("out_file", type=str, help="Output File Pathname")

    # Parse the command-line arguments
    args = arg_parser.parse_args()

    # Get the input and output file paths
    in_path = Path(args.in_file)
    out_path = Path(args.out_file)

    # Choose the program to run based on the provided argument
    if args.program == "quicksort1":
        # Open the input and output files
        with in_path.open('r') as input_file, out_path.open('w') as output_file:
            # Call the corresponding function and pass the input and output files
            function1(input_file, output_file)
            output_file.flush()
    elif args.program == "quicksort2":
        with in_path.open('r') as input_file, out_path.open('w') as output_file:
            function2(input_file, output_file)
            output_file.flush()
    elif args.program == "quicksort3":
        with in_path.open('r') as input_file, out_path.open('w') as output_file:
            function3(input_file, output_file)
            output_file.flush()
    elif args.program == "quicksort4":
        with in_path.open('r') as input_file, out_path.open('w') as output_file:
            function4(input_file, output_file)
            output_file.flush()
    elif args.program == "merge":
        with in_path.open('r') as input_file, out_path.open('w') as output_file:
            function5(input_file, output_file)
            output_file.flush()
    else:
        # Print an error message for an invalid program name
        print("Invalid program name. Please choose from quicksort1, quicksort2, or quicksort3.")


if __name__ == "__main__":
    main()
