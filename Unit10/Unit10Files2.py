from pathlib import Path
from shutil import copyfile
import os, send2trash

print(Path.cwd())

source_path = "/home/student1/Desktop/CIS164/Unit10/test123.txt"
destination_path = "/home/student1/Desktop/CIS164/Unit10/test321.txt"


new_file_path = copyfile(source_path, destination_path)

new_file = open(new_file_path)
print("\nCopied File Contents:\n" + new_file.read())

os.unlink(source_path)
send2trash.send2trash(destination_path)
