def slip142():
    with open('contentToRead.txt', 'r') as my_file:
        content_in_file = my_file.readlines()

    rev_file = open('rev_file.txt', 'w')


    for lines in content_in_file:
        rev_file.write(lines[::-1])


    print('Displaying contents in file: ')
    print(open('rev_file.txt', 'r').read())


slip142()
str = "Hello and welcome"
print(str[::-1])