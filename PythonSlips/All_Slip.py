#
import datetime


'''
1.	Write a Python program to print the following pattern.                      
1
2 3
4 5 6
7 8 9 10
'''
def slip1a():
    number = 1
    for i in range(1, 5):
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1
        print()

#slip1a()


'''
2.	Write a python program to accept string and remove the characters which have odd 
    index values of given string using user defined function.      
'''
def slip1b(str):
    new_str = ''
    for i in range(len(str)):
        if i % 2 == 0: new_str += str[i]
    return new_str
#my_str = input('Enter a string: ')
#print(f'Removed letters at odd index: {slip1b(my_str)}')



'''
    Print whether given num is armstrong or not
'''
def slip2a(num):
    temp = num
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum = sum + (rem * rem * rem)
        temp //= 10
    return sum == num
# num = int(input('Enter a number: '))
# print(f'Armstrong number?: {slip2a(num)}')





'''
    2.	Write a Python function that accepts a string and calculate the number of 
    upper case letters and lower case letters.                                                 
'''

def slip2b(str):
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


#slip2b("hello AND weLc O")




'''
	Write a python program to reverse a string
'''
def slip3a(str):
    reverse_str = ''
    n = len(str) - 1
    while n >= 0:
        reverse_str += str[n]
        n -= 1
    print(f'String entered: {str}')
    print(f'String reversed: {reverse_str}')


#slip3a("skrow siht os")




'''
2.	Write a Python program to check if a given key already exists in a dictionary.
 If key exists replace with another key/value pair
'''
dict = {"apple": 1, "banana": 2, "orange": 3, "grape": 4}

def slip3d(key):
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


#slip3d("banana")




'''
1.	Write a Python Program to Check if given number is prime or not.
 Also find factorial of the given number using user defined function.
'''

def slip4a(n):
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


# slip4a(4)




'''
Write a python script to define a class student having members roll no, name, age, gender. 
Create a subclass called Test with member marks of 3 subjects. 
Create three objects of the Test class and display all the details of the student with total marks.                                                                                   

'''
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



'''
1.	Write an anonymous function to find area of square and rectangle
'''
square = lambda s: print(f'Area of square of {s} side is {s*s}')
rectangle = lambda l, b: print(f'Area of rectangle of l {l} and b {b} is {l*b}')

def slip5a():
    s, l, b = input('Enter side of square and length and breadth of rectange:').split()
    square(int(s))
    rectangle(int(l), int(b))

#slip5a()



'''
1.	Create a list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a python program that prints out
 all the elements of the list that are less than 5. 
'''
def slip6a(my_list):
    for num in my_list:
        if num < 5:
            print(my_list[num])

# slip6a([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])






'''
2.	Write a Python class which has two methods get_String and print_String.
 get_String accept a string from the user and print_String prints the string in upper case. 
Further modify the program to reverse a string word by word and print it in lower case.                                                                        
'''
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


def slip6b():
    Ts1 = Testing_String()
    Ts1.get_string(input('Enter a string: '))
    Ts1.print_string()

#slip6b()






'''
	Write a Python program to accept n numbers in list and remove duplicates from a list.                                                                                                 
'''
def slip7a():
    mylist = list(map(int, input().split()))
    print(mylist)

    final_list = []
    for num in mylist:
        if num not in final_list:
            final_list.append(num)
    
    print(f'Removed duplicates: {final_list}')

# slip7a()




'''
	Write a python script to define the class Person having members name, address.
 Create a subclass called Employee with member salary.
 Create 'n' objects of the Employee class and display all the details of the employees.
'''
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

    for _ in range(n):
        Employees.append(get_employee())

    print('Displaying employee records: ')
    for emp in Employees:
        emp.display_details()

#slip7b()







'''
	Write a  Python program that encrypts a message by adding a key value to every character.  
'''
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

def slip8a():
    msg = input('Enter a message: ')
    key = 5
    alphabets = "abcdefghijklmnopqrstuvwxyz "
    enc_msg =  encrypt_msg(alphabets, msg, key)
    decrypt_msg(alphabets, enc_msg, key)

# slip8a()




'''
	Write a Python script using class, which has two methods get_String and print_String.
 get_String accept a string from the user and print_String print the string in upper case                                                                             
'''
class string_class:
    def get_string(self, str):
        self.str = str

    def print_string(self):
        print(f'Converted to upper case: {self.str.upper()}')

def slip8b():
    str = input('Enter a string: ')
    s1= string_class()
    s1.get_string(str)
    s1.print_string()

#slip8b()




'''
	Write a python script to find the repeated items of a tuple. tup=(1,2,2,3,4,4)    
'''
def slip9a():
    tup = (1, 2, 2, 3, 4, 4, 3)
    mylist = []
    print('Repeated Numbers in tuple: ', end="")

    for x in tup:
        if tup.count(x) > 1 and x not in mylist:
            mylist.append(x)
            print(x, end=" ")

#slip9a()




'''
Write a python program to count repeated characters in a string. 
Sample string: 'thequickbrownfoxjumpsoverthelazydog' 
Expected output: o-4, e-3, u-2, h-2, r-2, t-2                                           
'''
def slip9b():
    mylist = []
    str = 'thequickbrownfoxjumpsoverthelazydog'
    for letter in str:
        if str.count(letter) > 1 and letter not in mylist:
            print(f'{letter}: {str.count(letter)}', end=" ")
            mylist.append(letter)

    # OR

    my_dict = {}
    for letter in str:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
    print()
    for key in my_dict:
        if my_dict[key] != 1:
            print(f'{key}:{my_dict[key]} ', end="")


#slip9b()



'''
Write a Python program to implement the concept of queue using list
'''
class Queue_list:
    def __init__(self):
        self.my_queue = []
        print('Queue constructed..')

    def enqueue(self, x):
        self.my_queue.append(x)

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


def slip10a():
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


#slip10a()




'''
 	Write a python program to count number of upper case letters, 
 small case letters, digits in the file.                                                                            
'''

def slip10b():
    file = open('my_text.txt', 'r')

    lower_case = 0
    upper_case = 0
    digits = 0
    for line in file:
        print(line)
        for char in line:
            if char.islower(): lower_case += 1
            elif char.isupper(): upper_case += 1
            elif char.isdigit(): digits += 1

    file.close()
    print(f'Lower case: {lower_case}, Upper case: {upper_case}, digits: {digits}')

#slip10b()



'''
	Write a  Python program that counts the number of occurrences of a character in a string.                                                                                                  
'''
def slip11a(str):
    my_dict = {}
    for letter in str:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
    print(my_dict)

#slip11a('couting no.of occurrences of each char')





'''
	Write a Python script to generate and print a dictionary which contains a number (between 1 and n) in the form(x:x*x).
 Sample Dictionary (n=5) Expected Output: {1:1, 2:4, 3:9, 4:16, 5:25}                                                                                            
'''
def slip12a():
    n = int(input('Enter n: '))
    my_dict = {}
    for i in range(1, n+1):
        my_dict[i] = i*i

    print('Displaying dictionary: ')
    print(my_dict)
    print({i : i*i for i in range(1, n+1)})

#slip12a()





'''
	Write a python script to implement bubble sort using list.                   
'''
def bubbleSort(num_list):
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                temp = num_list[j]
                num_list[j] = num_list[j + 1]
                num_list[j + 1] = temp

    print(num_list)


def slip13a():
    num_list = list(map(int, input('Enter numbers:').split()))
    bubbleSort(num_list)
    print(num_list)

#slip131()






'''
	Write a python script to create a class Rectangle with data member’s length, width and methods area, perimeter
 which can compute the area and perimeter of rectangle
 '''
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

def slip13b():
    r1 = Rectangle(int(input('Length: ')), int(input('Width: ')))
    print(r1.perimeter())
    print(r1.area())

#slip13b()





'''
	Write a Python program to convert a tuple of string values to a tuple of integer values.
Original tuple values: (('44', '444'), ('1516', '45')) New tuple values: ((44, 444), (1516, 45))
'''
def convert_to_int(my_tuple):
    my_tuple = tuple(int(e) for e in my_tuple)
    print(my_tuple)

def slip14a():
    my_tuple = (('141', '45'), ('21', '90'))
    my_tuple = tuple(map(convert_to_int, my_tuple))
    print(tuple(tuple(map(int, i) for i in my_tuple)))

# slip14a()





'''
	Write a Python program to accept two lists and merge the two lists into list of tuple
'''
def slip15a():
    list1 = list(map(int, input('Enter first list: ').split()))
    
    list2 = list(map(int, input('Enter second list: ').split()))

    my_tuple = tuple(list1 + list2)
    print(my_tuple)

#slip15a()






'''
	Write a python program to create a class Circle and compute the Area and 
the circumferences of the circle.(use parameterized constructor)                                                                                    
'''

class MyCircle:
    def __init__(self, r):
        self.r = r

    def area_circle(self):
        return 3.14*self.r*self.r

    def circum_circle(self):
        return 2*3.14*self.r


def slip15b():
    r = float(input('Enter radius of circle: '))
    c = MyCircle(r)
    print(f'Circumference of circle: {c.circum_circle()}')
    print(f'Area of circle: {c.area_circle()}')

# slip15b()







'''
	Write a Python script to sort (ascending and descending order)  a dictionary by key
'''

def slip16a():
    my_dict = {89: 'Bugatti', 2: 'Porsche', 3: 'BMW', 54: 'Lexus', 23: 'Ferrari', -4: 'Tesla'}
    for k in sorted(my_dict):
        print(f'{k} : {my_dict[k]}')
    print()
    for k in reversed(sorted(my_dict)):
        print(f'{k} : {my_dict[k]}')

# slip16a()






'''
	Define a class named Shape and its subclass Square. 
The subclass has an init function which takes an argument Length. 
Both classes should have methods to calculate area and perimeter of a given shape.                                                                       
'''
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

def slip16b():
    len = int(input('Enter length: '))
    sq = Square(len)
    print(f'Area of square {sq.sq_area()}')
    print(f'Perimeter of square: {sq.sq_perimter()}')

#slip16b()






'''
	Write a Python program to unzip a list of tuples into individual lists.
                 L= [(1,2), (3,4), (8,9)]
'''
def slip17a():
    l = [(1, 2), (3, 4), (5, 6)]
    l = list(map(list, l))
    for lis in l:
        print(lis)

# slip17a()







'''
	Write Python program that has a class Person storing name and date of birth(DOB) of a person. Subtract the DOB from today’s date
 to find out whether a person is eligible to vote or not
 '''
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

def slip17b():
    name = input('Enter Name: ')
    dob = input('Enter date of birth (d:m:y): ').split()
    dob = list(map(int, dob))
    p1 = Person(name, dob)
    print(p1.is_eligible())

# slip17b()





'''
	Write a Python program to compute element-wise sum of given tuples.
        Original tuples: (1, 2, 3, 4) (3, 5, 2, 1) (2, 2, 3, 1)
        Element-wise sum of the said tuples: (6, 9, 8, 6) 

'''
def slip18a():
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

#slip18a()






