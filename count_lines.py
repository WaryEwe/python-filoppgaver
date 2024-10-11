def count_lines_file():
    file = input('Enter the name of your file: ')
    with open(file, 'r') as f:
        lines = sum(1 for l in f)
    print(f'The file {file} have {lines} lines')

count_lines_file()
