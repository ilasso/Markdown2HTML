#!/usr/bin/python3
"""
module:markdown2html
script that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name

Requirements:

If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0

"""

from sys import argv
from sys import stdout
from sys import stderr
import os
if __name__ == "__main__":
    if len(argv) != 3:
        stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if not os.path.isfile(argv[1]):
        stderr.write("Missing <filename>")
        exit(1)
    exit(0)
