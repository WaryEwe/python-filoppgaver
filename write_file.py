def write_file():
    file_text = input('Enter the text you want to write: ')
    file_name = input('Enter the name of your file: ')
    file = open(file_name, 'w')
    file.write(file_text)

write_file()
