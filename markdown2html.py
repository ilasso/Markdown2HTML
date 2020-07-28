#!/usr/bin/python3
"""
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
