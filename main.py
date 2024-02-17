# name = "Aryan"
# print("Hi there, ", name)

# i = int(input("enter the first number:"))
# print(i6)
# j = int(input("enter the second number: "))
# pri4nt(j)

# k = i // j
# print(k)


""" 
Your python file is written in human readable language.

python main.py

Python file -> [Syntax checker and translator] -> Syntax error messages
        (Byte code)     ↓  ↓  ↓  ↓  ↓  ↓ 
     User input -> [Python Virtual Machine (PVM)] -> other error message (runtime error)
    (Program output)    ↓  ↓  ↓  ↓  ↓  ↓


Datatypes:

1. Integer int() -> -2^31 to (2^31-1)                                                                                                                                   IMMUTABLE          
2. Float float() -> -10^308 to (10^308), 16 digits of precision                                                                                                         IMMUTABLE
3. Character -> ord('H'), chr(97)                                                                                                                                       IMMUTABLE                                                                                                                          
4. String "H" str()                                                                                                                                                     IMMUTABLE
5. Tuple i= (10,90,23)                                                                                                                                                     IMMUTABLE
6. Boolean                                                                                                                                                              IMMUTABLE
7. List i = [10,20] "elements can be repeated"                                                                                                                          MUTABLE
8. dictionary               student = {'name': 'John', 'age': 35}                                                                                                       MUTABLE
9. set                      i = {10, 23, 35, 675} "only unique element, new elements can be inserted, old elements can be removed"                                      MUTABLE
10. frozen_set              i = {10, 23, 35, 675}   j = frozenset(i)    "only unique elements, new elements CANNOT be inserted, old elements CANNOT be removed"         IMMUTABLE


IMMUTABLE vs MUTABLE datatypes 

3.78       3.78 * 10^0      3.78e0
37.8       3.78 * 10^1      3.78e1
0.000378   3.78 * 10^-4     3.78e-4

"""

# a = 'a'
# print(ord(a)) # gives the ASCII value of the character

# c = 100
# print(chr(c)) # gives the UNICODE/character value of ASCII

# Arithmetic Expression

''' Arithmetic Operators

**  -> Exponentiation           a**b ; a^b

-   -> Negation                 a = 10; -a = -10

*   -> Multiplication           a*b
/   -> Division                 a/b (decimal division)
//  -> Quotient                 a//b (integer division)
%   -> Remainder or modulus     a%b

+   -> Addition                 a+b
-   -> Subtraction              a-b
'''


# 5 + 3 * 2 ** 3 / 2 // 7 ----> 6
# 5 + 3 * 8 / 2 // 7
# 5 + 24 / 2 // 7
# 5 + 12 // 7
# 5 + 1
# 6

# 3 / 4 ** 3 % 0 + 34 ----------> Err: cannot divide by 0 

'''
Data conversion:

int()   int(35.31)  35
        int(35.78)  35
        int("35")   35

float() float(22)   22.0
        float("2")  2.0

str()   str(99)     '99'
        str(35.0)   '35.0' 


round(35.78) 36
'''

# print(4 + 5.0) # 9.0


"""
1. Let x=8 and y = 2. Write the values of the following expressions:
a. x + y * 3 ------- 14 ✔
b. (x + y) * 3 ------- 30 ✔
c. x ** y ---------- 64 ✔
d. x % y --------- 0 ✔
e. x / 12.0 ------- 0.0 ✗
f. x // 6 ------- 1 ✔

2. Let x = 4.66. Write the values of the following expressions:
a. round(x) 5   ✔
b. int(x) 4     ✔


"""

# i = (10, 23, 34, 45)
# # print(i.count(23))
# # print(i)

# j = [10, 23, 65, 98, 5, 35, 67]
# print(j)
# j.insert(3,45)  # inserts element at given index
#       # clears the list
# print(j)
# j.append(34)    # appends element at the end of the list
# print(j)   # [10, 23, 65, 45, 98, 5, 35, 67, 34] 
# frequency_of_5 = j.count(5)
# print(frequency_of_5)
# print(j.index(5))

# last_element = j.pop()
# print(j)
# print(last_element)

# j.remove(98)
# print(j)

# j.reverse()
# print(j)

# j.sort(reverse=False) # ascending
# print(j)


# i = ("api", 1, "23", 'a', 10.43)

# print(i[0])

# map = {}
# map["12"] = "twelve"
# map["13"] = "Thirteen"

# print(map)

# for index in range(1, 11):
#     print(index)



# print numbers from 10 to 1

#  for i in range(10,0,-1):
  #      print(i)

# take an input and print numbers from 1 to input in multiples of 2
# e.g., 
# Enter a number: 23
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22
# n = int(input("Enter a Number :"))
# for i in range(1,n):
#         i=i * 2
#         print(i)

# n = int(input("Enter a Number :"))
# for i in range(2, n, 2):
#         print(i)

# take an input and print numbers from 1 to input as odd numbers
# e.g., 
# Enter a number: 23
# 1, 3, 5, 7, 9, 11, ...., 23
# n = int(input("Enter a Number :"))
# for i in range(1, n+1, 2):
#         print(i)



#n = int(input("Enter a number: "))
#i = 1
#while i <= n:
 #       print(i)
 #       i+=2

# n = int(input("enter a no. : "))
# i = 2
# while i<=n:
#         print(i)
#         i+=2

# fibonacci sequence
# n = 23
# 0,1,1,2,3,5,8,13,21
# first = 0, second = 1, third = first + second, first = second, second = third
# first = 0 
# second = 1 
        
# n = int(input("enter a limit:"))
# first = 0
# second = 1
# print(first)
# print(second)

# while (first+second) <= n:
#         third = first + second
#         first = second
#         second = third
#         print(third)



# tribonacci sequence
# n = 23
# 0, 1, 1, 2, 4, 7, 13
# n = int(input("Enter a no. : "))  
# first = 0
# second = 1
# third = 1
# print(first) 
# print(second)
# print(third) 
# while (first+second+third) <= n:
#     fourth = first + second + third
#     first = second
#     second = third
#     third = fourth
#     print(fourth)   

# write a program to display the sum of all odd number from 1 to 100

# sum = 0
# for i in range(1 , 100):
#     if i % 2 == 0:
#         continue
#     else:
#         sum = sum + i
# print(int(sum))       

# sum = 0
# for i in range(1, 100, 2):
#     sum += i
# print(sum)




# write a program that displays all numbers from 1 to 100 that are not divisible by 2 as well as 3
# for i in range(1 , 100):
#     if i % 2 != 0 and i % 3 != 0:
#         print(i)

# write a program to sort 3 numbers in descending order using if else statement
        
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# c = int(input("enter a number: "))

# # a is greatest a > b and a > c
# # b is greatest b > a and b > c
# greatest = 0
# big = 0
# small = 0

# if a > b and a > c:
#     greatest = a
# elif b > a and b > c:
#     greatest = b
# else:
#     greatest = c

# if a < b and a < c:
#     small = a
# elif b < a and b < c:
#     small = b
# else:
#     small = c

# big = (a + b + c) - (greatest + small)

# print(greatest, big, small)


# write a program to count the total number of digits in the given number

# number_of_digits = 0
# n = int(input("Enter a no. :"))
# while n != 0:
#     number_of_digits += 1
#     n = n // 10
# print(number_of_digits)
""" 
-> n = 121234218923948
n = n / 10 = 12123421892394
n = n / 10 = 1212342189239
n = n / 10 = 121234218923
n = n / 10 = 12123421892
....
n = n / 10 = 1
n = n / 10 = 0


 """

# write a program to sum of digits in the given number
""" 
n -> 2390812903
-> 2+3+9+0+8+1+2+9+0+3=37
n


 """
# r = 0
# sum_of_digits = 0
# n = int(input("Enter a no. :"))
# while n!=0:
#     r = n % 10
#     sum_of_digits += r
#     n = n // 10

# print(sum_of_digits)



# write a program to calculate the sum and average of first n natural numbers
# sum = 0
# average = 0
# count = 0
# n = int(input("Enter a no.: "))
# for i in range(1,n+1):
#     sum += i
# print(sum)
# average = sum / n
# print(average)



""" 
write a program to calculate grade of a student:

100 - 91 -> grade A
81 - 90  -> grade B
71 - 80  -> grade C
61 - 70  -> grade D
51 - 60  -> grade E
<= 50    -> grade F

"""
# marks = float(input("enter marks of student:"))
# if marks <= 100 and marks >=91:
#     print("Grade A")
# elif marks <= 90 and marks >=81:
#     print("Grade B")
# elif marks <= 80 and marks >=71:
#     print("Grade C")  
# elif marks <= 70 and marks >=61:
#     print("Grade D") 
# elif marks <= 60 and marks >=51:
#     print("Grade E") 
# else:
#     print("Grade F")    


""" 
*
* *
* * *
* * * *
* * * * *
 """

# for i in range(1,6): 
#     for j in range (1, i+1):
#         print("* ", end="")
#     print()
    
""" 
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
"""

# for i in range(1 , 6):
#         for j in range(1 , i+1):
#                 print(j, " ", end="")
#         print()
        





""" 
1 2 3 4 5
1 2 3 4 
1 2 3 
1 2
1 

"""
# for i in range(6 , 1 , -1):
#     for j in range(1 , i):
#         print(j, " ", end="")
#     print()      



# WAP to swap two variables
# a -> 10
# b -> 12
# a = 12, b = 10 
# a , b = 12 , 10
# c , d = 0 , 0
# c = a 
# d = b
# a = (a + b) - a 
# b = c
# print("a =", a)
# print("b =", b)

# b = a + b
# a = b - a
# b = b - a 
# print("a =", a)
# print("b =", b)

# wap to decimal to binary, octal and hexadecimal:
binary = ""

n = 123
while n != 0:
        bit = n % 2
        binary = str(bit) + binary
        n //= 2
print(binary)


""" 
123 % 2 = 1; n = 123//2 = 61                     binary = "1"
61 % 2 = 1; n = 61 // 2 = 30                                    binary = "1" + "1" = "11"
30 % 2 = 0; n = 30 //2 = 15                                     binary = "0" + "11" = "011"
15 % 2 = 1; n = 15 // 2 = 7                                      binary = "1" + "011" = "1011"
7 % 2 = 1; n = 7 // 2 = 3                                                       binary = "1" + "1011" = "11011"
3 % 2 = 1; n = 3 // 2 = 1                                                      binary = "1" + "11011"= "111011"
1 % 2 = 1; n = 1 // 2 = 0===+                                                     binary = "1" + "111011" = "1111011"
"""
