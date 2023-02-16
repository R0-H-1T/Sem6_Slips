import os  # required module for deleting files


if os.path.exists('file1.txt'):
    os.remove('file1.txt')
    os.remove('file2.txt')


def create_file():
    file1 = open('file1.txt', 'w')
    file2 = open('file2.txt', 'w')
    file1.write(input('Enter details in file1.txt: '))
    file2.write(input('Enter details in file2.txt: '))
    file1.close()
    file2.close()
    print(open('file1.txt', 'r').read())
    print(open('file2.txt', 'r').read())


def merge_file_into_new_file():
    if os.path.exists('file3.txt'):
        os.remove('file3.txt')
    content_in_file1 = open('file1.txt', 'r').readlines()
    content_in_file2 = open('file2.txt', 'r').readlines()

    file3 = open('file3.txt', 'w')
    for lines in content_in_file1:
        file3.write(lines)

    for lines in content_in_file2:
        file3.write(lines)

    file3.close()
    print(open('file3.txt', 'r').read())


def delete_all_files():
    if(os.path.exists('file1.txt')):
        os.remove('file1.txt')
        os.remove('file2.txt')
        os.remove('file3.txt')
        print('All files successfully deleted')

create_file()
merge_file_into_new_file()
delete_all_files()
