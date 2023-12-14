#This script compares the outputs produced by the program for the sample inputs with the sample solutions
#Place both the sample solutions and the outputs on the root folder of this script

import filecmp

output_files = ["Sample Inputs/input1_output.txt", "Sample Inputs/input2_output.txt", "Sample Inputs/input3_output.txt", "Sample Inputs/input_hex1_output.txt", "Sample Inputs/input_hex2_output.txt", "Sample Inputs/input_hex3_output.txt"]
solution_files = ["Sample Solutions/solution1.txt", "Sample Solutions/solution2.txt", "Sample Solutions/solution3.txt","Sample Solutions/solution_hex1.txt","Sample Solutions/solution_hex2.txt","Sample Solutions/solution_hex3.txt"]

for i in range(len(output_files)):
    print("Test {}".format(i))
    if (not filecmp.cmp(output_files[i], solution_files[i])):
        print("Correct Solution")
    else:
        print("Incorrect Solution")
        