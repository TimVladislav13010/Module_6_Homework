from pathlib import Path
import re
import sys


def sorter(path=sys.argv[1]):
    path = Path(path)
    for i in path.iterdir():
        
        if i.is_dir():
            print(f"This is dir: {i}")
            sorter(path / i)
        if i.is_file():
            print(f"This is file: {i}")
            path = path / i
            format_files = path.suffix
            print(format_files)
            if format_files == ".txt":
                print(f"This is text file {format_files}")
                file_name = path.name
                append_file_lists(format_files, file_name)
                

                
def append_file_lists(format_files, file_name):
    text_file = []

    if format_files == ".txt":
        text_file.append(file_name)

    
    return text_file

if __name__ == "__main__":

    pass


sorter()
