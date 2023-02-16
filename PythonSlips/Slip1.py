#
import datetime


def print_pyramid():
    number = 1
    for i in range(1, 5):
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1
        print()


def remove_odd_index(str):
    new_str = ''
    for i in range(len(str)):
        if i % 2 == 0: new_str += str[i]
    return new_str


# input_str = input('Enter a string: ')
# print(f'Removed letters at odd index: {remove_odd_index(input_str)}')


def is_armstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum = sum + (rem * rem * rem)
        temp //= 10
    return sum == num


# num = int(input('Enter a number: '))
# print(f'Armstrong number?: {is_armstrong(num)}')

# UPPERCASE AND LOWERCASE LETTERS COUNT

def lowercase_and_uppercase_count(str):
    d = {"Uppercase": 0, "Lowercase": 0}
    for ch in str:
        if ch.isupper():
            d["Uppercase"] += 1
        elif ch.islower():
            d["Lowercase"] += 1
        else:
            pass
    print(f'String entered {str}')
    print(f'Uppercase Letters: {d["Uppercase"]}')
    print(f'Lowercase Letters: {d["Lowercase"]}')


# lowercase_and_uppercase_count("hello AND weLc O")


# REVERSE STRING
def reverse_string(str):
    reverse_str = ''
    n = len(str) - 1
    while n >= 0:
        reverse_str += str[n]
        n -= 1
    print(f'String entered: {str}')
    print(f'String reversed: {reverse_str}')


# reverse_string("skrow siht os")

# CHECK IF KEY ALREADY EXITS IN DICTIONARY, IF EXISTS REPLACE WITH
# ANOTHER KEY/VALUE

dict = {"apple": 1, "banana": 2, "orange": 3, "grape": 4}


def check_key(key):
    print(dict)
    if key in dict:
        print(f'Is present: {key} : {dict[key]}')
        # dict.pop(key)
        k, v = input("Enter a key and its value to replace:").split()
        dict[k] = dict.pop(key)
        dict[k] = v
        print(f'Updated dictionary: {dict}')
    else:
        print("Key not present")


# check_key("banana")

# 1.CHECK IF NUMBER PRIME OR NOT
# 2.FIND FACTORIAL OF NUMBER

def prime_and_factorial(n):
    choose = input('Prime(p) or factorial(f): ')
    if choose.upper() == 'P':
        flag = False
        if n == 1:
            print(n, "is not a prime number")
        elif n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    flag = True
                    break
            if flag:
                print(n, "is not a prime number")
            else:
                print(n, "is a prime number")

    elif choose.upper() == 'F':
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(f'factorial of a {n} is {fact}')
    else:
        print('Invalid key entered.')


# prime_and_factorial(4)


# CLASS Student and Test
class Student:
    def __init__(self, rollno, name, age, gender):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.gender = gender


class Test(Student):
    def __init__(self, rollno, name, age, gender, m1, m2, m3):
        super().__init__(rollno, name, age, gender)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_marks(self):
        self.total = self.m1 + self.m2 + self.m3
        print(f'Student: {self.rollno}, {self.name}, {self.age}, {self.gender}')
        print(f'Marks obtained: {self.m1}, {self.m2}, {self.m3}\nTotal: {self.total}\n')


t1 = Test(1, 'Rohit', 12, 'M', 43, 87, 65)
t2 = Test(2, 'Christin', 17, 'F', 67, 45, 83)
t3 = Test(3, 'Neil', 16, 'M', 60, 91, 96)

# t1.get_marks()
# t2.get_marks()
# t3.get_marks()

# ANONYMOUS FUNCTION TO FIND AREA OF SQUARE AND RECTANGLE

square = lambda s: print(f'Area of square of {s} side is {s*s}')
rectangle = lambda l, b: print(f'Area of rectangle of l {l} and b {b} is {l*b}')

# s, l, b = input('Enter side of square and length and breadth of rectange:').split()
# square(int(s))
# rectangle(int(l), int(b))


# CREATE A LIST THAT PRINTS OUT ALL THE NUMBERS THAT ARE < 5

def less_than_5_in_list(my_list):
    for num in my_list:
        if num < 5:
            print(my_list[num])

# less_than_5_in_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

class Testing_String:
    def get_string(self, user_str):
        self.user_str = user_str

    def print_string(self):
        print(f'Upper case: {self.user_str.upper()}')
        self.user_str = self.user_str.split()
        len_str = len(self.user_str) - 1
        print('Revering string and in lower case: ')
        str123 = ""
        while len_str >= 0:
            str123 = str123 + self.user_str[len_str].lower() + " "
            len_str -= 1
        print(str123)

# Ts1 = Testing_String()
# Ts1.get_string(input('Enter a string: '))
# Ts1.print_string()

def slip_71():
    n = int(input('Enter total numbers:'))
    if n == 0 : exit(0)

    mylist = input().split()
    mylist = list(map(int, mylist))
    print(mylist)

    final_list = []
    count = 0
    for num in mylist:
        if num not in final_list:
            final_list.insert(count, num)
            count += 1
        else:
            pass
    print(f'Removed duplicates: {final_list}')


# slip_71()

class Person:
    def __init__(self, name, address):
        self.name = name;
        self.address = address

class Employee(Person):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.salary = salary

    def display_details(self):
        print(f'{self.name}, {self.address}, {self.salary}')


def get_employee():
    name, address, salary =  input('Enter Name, Address and Salary: ').split()
    return Employee(name, address, salary)

def slip7b():
    Employees = []
    n = int(input('Enter number of employees: '))
    if n == 0:
        exit(0)
    if n == 1:
        Employees.insert(0, get_employee())

    Employees.insert(0, get_employee())
    for i in range(1, n):
        Employees.append(get_employee())

    print('Displaying employee records: ')
    for emp in Employees:
        print(emp.display_details())

# slip7b()

# ENCRYPT A MESSAGE USING KEY VALUE PAIR

def encrypt_msg(alphabets, msg, key):
    encrypted = ""
    # alphabets.find(letter) // returns index of the letter
    for letter in msg:
        new_position = (alphabets.find(letter) + key) % len(alphabets) #creating a new index
        encrypted += alphabets[new_position]  # finding the letter at that index and adding it to encrypted

    print(f'Encrypted Message: {encrypted}, {len(alphabets)}')
    return encrypted

def decrypt_msg(alphabets, msg, key):
    decrypted = ""
    for letter in msg:
        new_position = (alphabets.find(letter) - key) % len(alphabets)  # creating a new index
        decrypted += alphabets[new_position]  # finding the letter at that index and adding it to encrypted

    print(f'Decrypted Message: {decrypted}')
    return decrypted

def slip81():
    msg = input('Enter a message: ')
    key = 5
    alphabets = "abcdefghijklmnopqrstuvwxyz "
    enc_msg =  encrypt_msg(alphabets, msg, key)
    decrypt_msg(alphabets, enc_msg, key)

# slip81()

# CLASS THAT HAS TWO METHODS 1.GET INPUT FORM USER 2.DISPLAY
# IT IN UPPER CASE

class string_class:
    def get_string(self, str):
        self.str = str

    def print_string(self):
        print(f'Converted to upper case: {self.str.upper()}')

def slip82():
    str = input('Enter a string: ')
    s1= string_class()
    s1.get_string(str)
    s1.print_string()

#slip82()

# SCRIPT TO FIND REPEATED ITEMS OF  TUPLE
def find_repeated_items_in_tuple():
    tup = (1, 2, 2, 3, 4, 4, 3)
    mylist = []
    print('Repeated Numbers in tuple: ')
    # OR, although this is better:)
    for x in tup:
        if tup.count(x) > 1 and x not in mylist:
            mylist.append(x)
            print(x)
    print(mylist)
    #print(f'Duplicates in tuple: {[ num for num in tup if tup.count(num) > 1]}')

# find_repeated_items_in_tuple()

# FIND COUNT OF REPEATED CHARACTER IN STRING AND DISPLAY IT
def find_count_of_repeated_chs():
    mylist = []
    str = "tttthhhhheeeennnnoooottttt"
    for letter in str:
        if letter not in mylist:
            print(f'{letter}: {str.count(letter)}', end=" ")
            mylist.append(letter)

    # OR

    my_dict = {}
    for letter in str:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
    print(f'\n{my_dict}')

# find_count_of_repeated_chs()

class Queue_list:
    def __init__(self):
        self.my_queue = []
        print('Queue constructed..')

    def enqueue(self, x):
        self.my_queue.insert(0, x) if len(self.my_queue) <= 0 else self.my_queue.append(x)

    def dequeue(self):
        if len(self.my_queue) <= 0:
            print('Noting in the queue')
            exit(0)
        self.my_queue.remove(self.my_queue[0])

    def queue_peek(self):
        if len(self.my_queue) <= 0:
            print('Nothing in the queue')
            exit(0)
        print(f'Peek: {self.my_queue[0]}')

    def display_queue(self):
        if len(self.my_queue) <= 0:
            print('Nothing in the queue')
        print(self.my_queue)

    def queue_count(self):
        print(f'Total elements in queue: {len(self.my_queue)}')


def slip101():
    q = Queue_list()
    q.enqueue(23)
    q.display_queue()
    q.enqueue(8)
    q.enqueue(4)
    q.enqueue(67)
    q.enqueue(1)
    q.queue_peek()
    q.queue_count()
    q.display_queue()

    q.dequeue()
    q.display_queue()
    q.queue_peek()
    q.dequeue()
    q.dequeue()
    q.display_queue()
    q.enqueue(-55)
    q.display_queue()


#slip101()

# COUNT LETTER, NOS, UPPERCASE AND LOWERCASE IN A FILE

def slip102():
    file = open('my_text.txt', 'r')

    lower_case = 0
    upper_case = 0
    digits = 0
    for line in file:
        for char in line:
            if char.islower(): lower_case += 1
            elif char.isupper(): upper_case += 1
            elif char.isdigit(): digits += 1

    file.close()
    print(f'Lower case: {lower_case}, Upper case: {upper_case}, digits: {digits}')

# slip102()



# counts no.of occurrences of character in a string
def slip111():
    my_list = []
    str = input('Enter a string: ')
    for ch in str:
        if ch not in my_list:
            print(f' {ch} : {str.count(ch)}', end=" ")
            my_list.append(ch)
#slip111()





# PRINT A DICTIONARY FROM 1 to n [x : x*x*x]
def slip121():
    n = int(input('Enter n: '))
    my_dict = {}
    for i in range(1, n+1):
        my_dict[i] = i*i

    print('Displaying dictionary: ')
    print(my_dict)
    print({i : i*i for i in range(1, n+1)})

#slip121()

# BUBBLE SORT in PYTHON

def bubbleSort(num_list):
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                temp = num_list[j]
                num_list[j] = num_list[j + 1]
                num_list[j + 1] = temp

    print(num_list)


def slip131():
    num_list = list(map(int, input('Enter numbers:').split()))
    bubbleSort(num_list)
    print(num_list)

#slip131()



# Create a class Rectange with data members height and width
# and methods area, perimeter
class Rectangle:
    __length__ = 0
    __width__ = 0
    def __init__(self, l, w):
        self.__length__ = l
        self.__width__ = w

    def perimeter(self):
        return 2 * (self.__length__ + self.__width__)

    def area(self):
        return self.__length__ * self.__width__

def slip132():
    r1 = Rectangle(int(input('Length: ')), int(input('Width: ')))
    print(r1.perimeter())
    print(r1.area())

#slip132()



# TO conert tuple string into integer tuple
def convert_to_int(my_tuple):
    my_tuple = tuple(int(e) for e in my_tuple)
    print(my_tuple)

def slip141():
    my_tuple = (('141', '45'), ('21', '90'))
    my_tuple = tuple(map(convert_to_int, my_tuple))
    print(tuple(tuple(map(int, i) for i in my_tuple)))

# slip141()


# WRITE A PYTHON TO PROG TO ACCEPT TWO LIST AND MERGE IT INTO
# A LIST OF TUPLE


def slip151():
    list1 = input('Enter first list: ').split()
    list1 = list(map(int, list1))
    list2 = input('Enter second list: ').split()
    list2 = list(map(int, list2))

    my_tuple = tuple(list1 + list2)
    print(my_tuple)

# slip151()

# Create a class cricle to find out circumference and area of circle


class MyCircle:
    def __init__(self, r):
        self.r = r

    def area_circle(self):
        return 3.14*self.r*self.r

    def circum_circle(self):
        return 2*3.14*self.r


def slip152():
    r = float(input('Enter radius of circle: '))
    c = MyCircle(r)
    print(f'Circumference of circle: {c.circum_circle()}')
    print(f'Area of circle: {c.area_circle()}')

# slip152()

# SORT A DICTIONARY BY KEY - Ascending and Descending
def slip161():
    my_dict = {89: 'Bugatti', 2: 'Porsche', 3: 'BMW', 54: 'Lexus', 23: 'Ferrari', -4: 'Tesla'}
    for k in sorted(my_dict):
        print(f'{k} : {my_dict[k]}')
    print()
    for k in reversed(sorted(my_dict)):
        print(f'{k} : {my_dict[k]}')

# slip161()

class Shape:
    def __init__(self, l):
        self.l = l


class Square(Shape):
    def __init__(self, l):
        super().__init__(l)

    def sq_area(self):
        return self.l*self.l

    def sq_perimter(self):
        return 4*self.l

def slip162():
    len = int(input('Enter length: '))
    sq = Square(len)
    print(f'Area of square {sq.sq_area()}')
    print(f'Perimeter of square: {sq.sq_perimter()}')

#slip162()

def slip171():
    l = [(1, 2), (3, 4), (5, 6)]
    l = list(map(list, l))
    for lis in l:
        print(lis)

# slip171()

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def is_eligible(self):
        x = datetime.datetime.now()
        x = int(x.strftime('%Y'))
        if x - self.dob[2] >= 18:
            return True
        return False

def slip172():
    name = input('Enter Name: ')
    dob = input('Enter date of birth (d:m:y): ').split()
    dob = list(map(int, dob))
    p1 = Person(name, dob)
    print(p1.is_eligible())

# slip172()

def slip181():
    my_tuple = (1, 3, 4, 5), (2, 6, 8, 9), (5, 3, 6, 1)
    #
    # print(my_tuple)
    # my_list = [0, 0, 0, 0]
    # for tup in my_tuple:
    #     for i in range(len(tup)):
    #         my_list[i] += tup[i]
    #
    # print(tuple(my_list))

    my_zip = list(map(zip, my_tuple))
    print(my_zip)
    x = zip(x for x in my_tuple)
    print(x)

#slip181()



class MyEmployee:
    def accept_details(self, id, name, dept, sal):
        self.id = id
        self.name = name
        self.dept = dept
        self.sal = sal

    def display(self):
        print(f'{self.id}, {self.name}, {self.dept}, {self.sal}')


# class MyManager(MyEmployee):
    # def accept_details(self, id, name, dept, sal, bonus):
    #    super().__init__(id, name, dept, sal)



# Pickle python program to write and read a data from a
# file stating the position
# of the file object. (Using dump(), load() functions).
#https://www.youtube.com/source/bXocWfvja2Y/shorts?bp=8gU2CikSJwoLYlhvY1dmdmphMlkSC2JYb2NXZnZqYTJZGgtiWG9jV2Z2amEyWSj1otjhi4zM5YwB