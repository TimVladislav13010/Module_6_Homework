from pathlib import Path
import re
import sys


def sorter(path):
    path = Path(path)
    for i in path.iterdir():
        print(i.name)


if __name__ == "__main__":
    pass
     # sorter(r"E:\goit\Python education\Homework\Module_6_Homework\test_folder")


sorter(r"E:\goit\Python education\Homework\Module_6_Homework\test_folder")