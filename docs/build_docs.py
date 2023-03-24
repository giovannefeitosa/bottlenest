import os
import sys


def main():
    # sys.path.insert(0, os.path.abspath('src/bottlenest'))
    os.system("sphinx-build -b html docs dist-docs")
