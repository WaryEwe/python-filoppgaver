def append_file():
    file_name = input('Enter the name of your file: ')
    file_text = input('Enter the text you want to append to your file: ')
    file = open(file_name, 'a')
    file.write(file_text)

append_file()
