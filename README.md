# Nokia assignment
 This python script is used for the work-application assignment given by the representative at Nokia.

How to use:
    1. Save this script on the same directory that your Linux kernel ring buffer is.
    2. Run this script from the command line.

What this script does?:
    This script searches the kernel ring buffer for possible errors. When possible errors are detected, 
    the script prints out the line and then writes it down in to a *.txt file in JSON-format. 

Different options:
    -o, --output: This option allows the user to specify which directory the user wants the errors printed in.
    -u, --until: This option allows the user to specify the end date of the parsing.