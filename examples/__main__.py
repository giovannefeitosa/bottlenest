import examples
import os
import importlib
import sys
from . import *


def main():
    exampleName = sys.argv[1]
    sys.argv = sys.argv[1:]
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(getattr(examples, exampleName).main())
    # sys.exit(example.main())


if __name__ == "__main__":
    main()
