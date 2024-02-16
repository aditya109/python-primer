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

i = (10, 23, 34, 45)
# print(i.count(23))
# print(i)

j = [10, 23, 65, 98, 5, 35, 67]
print(j)
j.insert(3,45)  # inserts element at given index
      # clears the list
print(j)
j.append(34)    # appends element at the end of the list
print(j)   # [10, 23, 65, 45, 98, 5, 35, 67, 34] 
frequency_of_5 = j.count(5)
print(frequency_of_5)
print(j.index(5))

last_element = j.pop()
print(j)
print(last_element)

j.remove(98)
print(j)

j.reverse()
print(j)

j.sort(reverse=False) # ascending
print(j)