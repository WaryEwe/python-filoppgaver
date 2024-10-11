import os
import pathlib
def read_file():
    try:
        file = input('Enter the name of your file: ')
    except e as FileNotFoundException:
        print("The file dosen't exist")
        f = open(file, 'r')
    print(f.read())

read_file()
