# a = int(input("ener the first no."))
# b = int(input("ener the second no."))
# c = a+b 
# print(c)

# -----------------------------------------------------------------------------------------------------------------

# Q - 1

# nl =[]
# for i in range (1500,2701):
#     if (i% 7 == 0) and (i % 5 == 0):
#         nl.append(str(i))
# print(','. join(nl)) 

# -------------------------------------------------------------------------------------------------------------


# Q - 2 

# # Prompt the user to input a temperature in the format (e.g., 45F, 102C, etc.)
# temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")

# # Extract the numerical part of the temperature and convert it to an integer
# degree = int(temp[:-1])

# # Extract the convention part of the temperature input (either 'C' or 'F')
# i_convention = temp[-1]

# # Check if the input convention is in uppercase 'C' (Celsius)
# if i_convention.upper() == "C":
#     # Convert the Celsius temperature to Fahrenheit
#     result = int(round((9 * degree) / 5 + 32))
#     o_convention = "Fahrenheit"  # Set the output convention as Fahrenheit
# # Check if the input convention is in uppercase 'F' (Fahrenheit)
# elif i_convention.upper() == "F":
#     # Convert the Fahrenheit temperature to Celsius
#     result = int(round((degree - 32) * 5 / 9))
#     o_convention = "Celsius"  # Set the output convention as Celsius
# else:
#     # If the input convention is neither 'C' nor 'F', print an error message and exit the program
#     print("Input proper convention.")
#     quit()

# # Display the converted temperature in the specified output convention
# print("The temperature in", o_convention, "is", result, "degrees.")

# --------------------------------------------------------------------------------------------------------------

# Q - 3 

# # Import the 'random' module to generate random numbers
# import random

# # Generate a random number between 1 and 10 (inclusive) as the target number
# target_num, guess_num = random.randint(1, 10), 0

# # Start a loop that continues until the guessed number matches the target number
# while target_num != guess_num:5

#     # Prompt the user to input a number between 1 and 10 and convert it to an integer
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))

# # Print a message indicating successful guessing once the correct number is guessed
# print('Well guessed!')

#--------------------------------------------------------------------------------------------------------

# Q - 4 

# Set the value of 'n' to 5 (this will determine the number of lines in the pattern)
n = 5


# for i in range(n):
    
#     for j in range(i):
#            print('* ', end="")
  
#     print('')
# for i in range(n, 0, -1):
   
#     for j in range(i):
        
#         print('* ', end="")
    
#     print('') 


#---------------------------------------------------------------------------------------------------------------

# Q - 5 

# word = input("Input a word to reverse: ")


# for char in range(len(word) - 1, -1, -1):

#     print(word[char], end="")


# print("\n")

#-------------------------------------------------------------------------------------------------------------
#Q - 6 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# # Initialize counters for counting odd and even numbers
# count_odd = 0
# count_even = 0

# # Iterate through each element 'x' in the tuple 'numbers'
# for x in numbers:
#     # Check if the current number 'x' is even by evaluating 'not x % 2'
#     if not x % 2:  # If 'x' modulo 2 equals 0, it's even
#         # Increment the count of even numbers
#         count_even += 1
#     else:
#         # If 'x' modulo 2 doesn't equal 0, it's odd; increment the count of odd numbers
#         count_odd += 1

# # Print the total count of even and odd numbers
# print("Number of even numbers:", count_even)
# print("Number of odd numbers:", count_odd) 

#-------------------------------------------------------------------------------------------------------------
#Q - 7 
# # Create a list named 'datalist' containing various data types (int, float, complex, bool, string, tuple, list, dictionary)
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

# # Iterate through each item in the 'datalist'
# for item in datalist:
#     # Print the type of each item in the list along with the item itself
#     print("Type of", item, "is", type(item)) 

#-------------------------------------------------------------------------------------------------------------

#Q - 8 

# # Iterate through numbers from 0 to 5 using the range function
# for x in range(6):
#     # Check if the current value of 'x' is equal to 3 or 6
#     if (x == 3 or x == 6):
#         # If 'x' is 3 or 6, skip to the next iteration without executing the code below
#         continue
#     # Print the value of 'x' with a space and without a newline (end=' ')
#     print(x, end=' ')

# # Print a new line after printing all numbers satisfying the condition
# print("\n")

#-------------------------------------------------------------------------------------------------------------

#Q - 9 

# # Initialize variables 'x' and 'y' with values 0 and 1, respectively
# x, y = 0, 1

# # Execute the while loop until the value of 'y' becomes greater than or equal to 50
# while y < 50:
#     # Print the current value of 'y'
#     print(y)
    
#     # Update the values of 'x' and 'y' using simultaneous assignment,
#     # where 'x' becomes the previous value of 'y' and 'y' becomes the sum of 'x' and the previous value of 'y'
#     x, y = y, x + y
    
#------------------------------------------------------------------------------------------------------------

#Q - 10 

# # Iterate through numbers from 0 to 50 using the range function
# for fizzbuzz in range(51):
#     # Check if the current number is divisible by both 3 and 5 (i.e., divisible by 15)
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         # If divisible by both 3 and 5, print "fizzbuzz" and continue to the next iteration
#         print("fizzbuzz")
#         continue
#     # Check if the current number is divisible only by 3
#     elif fizzbuzz % 3 == 0:
#         # If divisible only by 3, print "fizz" and continue to the next iteration
#         print("fizz")
#         continue
#     # Check if the current number is divisible only by 5
#     elif fizzbuzz % 5 == 0:
#         # If divisible only by 5, print "buzz" and continue to the next iteration
#         print("buzz")
#         continue
#     # If the number is neither divisible by 3 nor 5, print the number itself
#     print(fizzbuzz) 
    
#------------------------------------------------------------------------------------------------------------

#Q - 11 
# # Prompt the user to input the number of rows
# row_num = int(input("Input number of rows: "))

# # Prompt the user to input the number of columns
# col_num = int(input("Input number of columns: "))

# # Create a 2D list (a list of lists) filled with zeros using list comprehension
# # The outer list will have 'row_num' elements and the inner lists will have 'col_num' elements
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# # Nested loop to populate the 2D list with multiplication results
# for row in range(row_num):
#     for col in range(col_num):
#         # Set the value at position [row][col] in the 2D list to the product of 'row' and 'col'
#         multi_list[row][col] = row * col

# # Print the resulting 2D list containing the multiplication table
# print(multi_list) 

#-------------------------------------------------------------------------------------------------------------

#Q - 12 

# lines = []

# # Continue to prompt the user for input indefinitely until a blank line is entered
# while True:
#     # Prompt the user to input a line of text
#     l = input()
    
#     # Check if the entered line is not empty (non-empty string)
#     if l:
#         # Convert the entered line to uppercase and append it to the 'lines' list
#         lines.append(l.upper())
#     else:
#         # If the entered line is empty, break out of the loop
#         break;

# # Iterate through each line in the 'lines' list
# for l in lines:
#     # Print each line (converted to uppercase) from the 'lines' list
#     print(l)

#______________________________________________________________________________________________________________________________________________________________________________________________________________




# PATTERN BASED EXERCISE OF PYTHON




#_______________________________________________________________________________________________________________________________________________________________________________--
# Q - 1
# rows = 6
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for i in range(rows):
#     # nested loop
#     for j in range(i):
#         # display number
#         print(i, end=' ')
#     # new line after each row
#     print('')

#-------------------------------------------------------------------------------------------------------------

#Q - 2

# rows = 5
# b = 0
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print('\r') 


#-------------------------------------------------------------------------------------------------------------

#Q - 3 
# rows = 5
# num = rows
# # reverse for loop
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print(num, end=' ')
#     print("\r")

#--------------------------------------------------------------------------------------------------------------

#Q - 4 
# rows = 5
# num = rows
# # reverse for loop
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print(num, end=' ')
#     print("\r")

#-------------------------------------------------------------------------------------------------------------

#Q - 5 

# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(0, i + 1):
#         print(j, end=' ')
#     print("\r")

#------------------------------------------------------------------------------------------------------------

#Q - 6 
# rows = 5
# i = 1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print((i * 2 - 1), end=" ")
#         j = j + 1
#     i = i + 1
#     print('') 

#--------------------------------------------------------------------------------------------------------------

#Q - 7 
# rows = 5
# i = 1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print((i * 2 - 1), end=" ")
#         j = j + 1
#     i = i + 1
#     print('')

#----------------------------------------------------------------------------------------------------------------

#Q - 8 
# rows = 5
# # reverse loop
# for i in range(rows, 0, -1):
#     num = i
#     for j in range(0, i):
#         print(num, end=' ')
#     print("\r")

#----------------------------------------------------------------------------------------------------------------

#Q - 9 

# rows = 6
# for i in range(1, rows):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print("")

#---------------------------------------------------------------------------------------------------------------

#Q - 10 

# rows = 5
# for i in range(0, rows + 1):
#     for j in range(rows - i, 0, -1):
#         print(j, end=' ')
#     print()

#--------------------------------------------------------------------------------------------------------------

#Q - 11 
# start = 1
# stop = 2
# current_num = stop
# for row in range(2, 6):
#     for col in range(start, stop):
#         current_num -= 1
#         print(current_num, end=' ')
#     print("")
#     start = stop
#     stop += row
#     current_num = stop

#------------------------------------------------------------------------------------------------------------------------

#Q - 12 
# rows = 6
# for i in range(1, rows):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print("") 

#----------------------------------------------------------------------------------------------------------------------------

#Q - 13 
# def print_pascal_triangle(size):
#     for i in range(0, size):
#         for j in range(0, i + 1):
#             print(decide_number(i, j), end=" ")
#         print()


# def decide_number(n, k):
#     num = 1
#     if k > n - k:
#         k = n - k
#     for i in range(0, k):
#         num = num * (n - i)
#         num = num // (i + 1)
#     return num

# # set rows
# rows = 7
# print_pascal_triangle(rows)

# ------------------------------------------------------------------------------------------------------------------

#Q - 14 
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, rows + 1):
#         if j <= i:
#             print(i, end=' ')
#         else:
#             print(j, end=' ')
#     print() 
 
#----------------------------------------------------------------------------------------------------------------------

#Q - 15 
# rowrows = 8
# # rows = int(input("Enter the number of rows "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         # multiplication current column and row
#         square = i * j
#         print(i * j, end='  ')
#     print()

#---------------------------------------------------------------------------------------------------------------------------

#Q - 16 
# number of rows
# rows = 5
# for i in range(0, rows):
#     # nested loop for each column
#     for j in range(0, i + 1):
#         # print star
#         print("*", end=' ')
#     # new line after each row
#     print("\r")

#---------------------------------------------------------------------------------------------------------------------------------------

#Q - 17 

# number of rows
# rows = 5
# k = 2 * rows - 2
# for i in range(0, rows):
#     # process each column
#     for j in range(0, k):
#         # print space in pyramid
#         print(end=" ")
#     k = k - 2
#     for j in range(0, i + 1):
#         # display star
#         print("* ", end="")
#     print("")

#----------------------------------------------------------------------------------------------------------------------------------------------------

# #Q - 18 
# rows = 5
# for i in range(rows + 1, 0, -1):
#     # nested reverse loop
#     for j in range(0, i - 1):
#         # display star
#         print("*", end=' ')
#     print(" ") 

#-----------------------------------------------------------------------------------------------------------------------------------------

#Q - 19 
# rows = 5
# k = 2 * rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")

#---------------------------------------------------------------------------------------------------------------------------------------

#Q - 20 
# rows = 5
# i = rows
# while i >= 1:
#     j = rows
#     while j > i:
#         # display space
#         print(' ', end=' ')
#         j -= 1
#     k = 1
#     while k <= i:
#         print('*', end=' ')
#         k += 1
#     print()
#     i -= 1 

#-------------------------------------------------------------------------------------------------------------------------------------------

#Q - 21 
# print("Print equilateral triangle Pyramid using asterisk symbol ")
# # printing full Triangle pyramid using stars
# size = 7
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     # decrementing m after each loop
#     m = m - 1
#     for j in range(0, i + 1):
#         print("* ", end=' ')
#     print(" ") 

#--------------------------------------------------------------------------------------------------------------------------------------------

#Q - 22 
# rows = 6
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")

# print(" ")

# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

#------------------------------------------------------------------------------------------------------------------------

#Q - 23 
# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")  

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 24 

# row
    # prints = 5
# i = 1
# while i <= rows:
#     j = i
#     while j < rows:
#         # display space
#         print(' ', end=' ')
#         j += 1
#     k = 1
#     while k <= i:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1

# i = rows
# while i >= 1:
#     j = i
#     while j <= rows:
#         print(' ', end=' ')
#         j += 1
#     k = 1
#     while k < i:
#         print('*', end=' ')
#         k += 1
# ('')
    # i -= 1
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q - 25  

# rows = 5
# i = 0
# while i <= rows - 1:
#     j = 0
#     while j < i:
#         # display space
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= rows - 1:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1

# i = rows - 1
# while i >= 0:
#     j = 0
#     while j < i:
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= rows - 1:
#         print('*', end=' ')
#         k += 1
#     print('')
#     i -= 1
 
#-----------------------------------------------------------------------------------------------------------------------------------------

#Q - 26 

# rows = 14
# print("*" * rows, end="\n")
# i = (rows // 2) - 1
# j = 2
# while i != 0:
#     while j <= (rows - 2):
#         print("*" * i, end="")
#         print("_" * j, end="")
#         print("*" * i, end="\n")
#         i = i - 1
#         j = j + 2 

#-----------------------------------------------------------------------------------------------------------------------------------

# #Q - 27 

# rows = 5
# k = 2 * rows - 2
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")
    
# k = rows - 2

# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("") 

#---------------------------------------------------------------------------------------------------------------------------------------

# #Q - 28 
# rows = 5
# i = 1
# while i <= rows:
#     j = rows
#     while j > i:
#         # display space
#         print(' ', end=' ')
#         j -= 1
#     print('*', end=' ')
#     k = 1
#     while k < 2 * (i - 1):
#         print(' ', end=' ')
#         k += 1
#     if i == 1:
#         print()
#     else:
#         print('*')
#     i += 1

# i = rows - 1
# while i >= 1:
#     j = rows
#     while j > i:
#         print(' ', end=' ')
#         j -= 1
#     print('*', end=' ')
#     k = 1
#     while k <= 2 * (i - 1):
#         print(' ', end=' ')
#         k += 1
#     if i == 1:
#         print()
#     else:
#         print('*')
#     i -= 1


#-----------------------------------------------------------------------------------------------------------------------------------

#Q - 29 
# ASCII number of 'A'
# ascii_number = 65
# rows = 7
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         character = chr(ascii_number)
#         print(character, end=' ')
#         ascii_number += 1
#     print(" ") 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 30 

# word = "Python"
# x = ""
# for i in word:
#     x += i
#     print(x) 


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 31 

# print("Print equilateral triangle Pyramid with characters ")
# size = 7
# asciiNumber = 65
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     m = m - 1
#     for j in range(0, i + 1):
#         character = chr(asciiNumber)
#         print(character, end=' ')
#         asciiNumber += 1
#     print(" ") 

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 32 

# # Same character pattern
# character = 'V'
# # convert char to ASCII
# char_ascii_no = ord(character)
# for i in range(0, 5):
#     for j in range(0, i + 1):
#         # Convert the ASCII value to the character
#         user_char = chr(char_ascii_no)
#         print(user_char, end=' ')
#     print()

#----------------------------------------------------------------------------------------------------------------------------

#Q - 33 
# Pyramid of horizontal tables of numbers
# rows = 10
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(i * j, end=' ')
#     print()  

#+------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 34 

# rows = 9
# for i in range(1, rows):
#     for j in range(-1 + i, -1, -1):
#         print(format(2 ** j, "4d"), end=' ')
#     print("")

#----------------------------------------------------------------------------------------------------------------------------------------

# #Q - 35 

# current_num = 1
# stop = 2
# rows = 3

# for i in range(rows):
#     for column in range(1, stop):
#         print(current_num, end=' ')
#         current_num += 1
#     print("")
#     stop += 2 

#----------------------------------------------------------------------------------------------------------------------------------------

#Q - 36 

# current_num = 1
# rows = 4
# stop = 2
# for i in range(rows):
#     for column in range(1, stop):
#         print(current_num, end=' ')
#         current_num += 1
#     print("")
#     stop += 1 

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 37 

# rows = 5
# last_num = 2 * rows
# even_num = last_num
# for i in range(1, rows + 1):
#     even_num = last_num
#     for j in range(i):
#         print(even_num, end=' ')
#         even_num -= 2
#     print("\r")

#----------------------------------------------------------------------------------------------------------------------------------------

#Q - 38 

# rows = 6
# for i in range(1, rows + 1):
#     for j in range(1, i - 1):
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
#     print()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q - 39 

# rows = 7
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print(i * j, end='  ')
#     print()

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 40 

# rows = 5
# for i in range(0, rows + 1, 1):
#     for j in range(i + 1, rows + 1, 1):
#         print(j, end=' ')
#     print() 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 41 

# rows = 6
# for i in range(0, rows):
#     for j in range(rows - 1, i, -1):
#         print(j, '', end='')
#     for l in range(i):
#         print('    ', end='')
#     for k in range(i + 1, rows):
#         print(k, '', end='')
#     print('\n') 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 42 
# row = 4
# for i in range(0, row):
#     c = 1
#     print(c, end=' ')
#     for j in range(row - i - 1, 0, -1):
#         print('*', end=' ')
#         c = c + 1
#         print(c, end=' ')
#     print('\n') 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 43 

# num = 4
# counter = 0
# for x in range(0, num):
#     for y in range(0, x + 1):
#         print(counter, end=" ")
#         counter = 2 ** (x + 1)
#     print() 


#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
   
   
# Practice problem

# numb = int(input(" Enter a number : "))    

  
  

# for a in range(1,11):    

#    print(numb,'x',a,'=',numb*a)

 #______________________________________________________________________________________________________________________________________________________________________________________________________________
 
 
 
 
 
 #Function based python program 
 
 
 
 
 
 
 
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#Q - 1 

# # Define a function that returns the maximum of two numbers
# def max_of_two(x, y):
#     # Check if x is greater than y
#     if x > y:
#         # If x is greater, return x
#         return x
#     # If y is greater or equal to x, return y
#     return y

# # Define a function that returns the maximum of three numbers
# def max_of_three(x, y, z):
#     # Call max_of_two function to find the maximum of y and z,
#     # then compare it with x to find the overall maximum
#     return max_of_two(x, max_of_two(y, z))

# # Print the result of calling max_of_three function with arguments 3, 6, and -5
# print(max_of_three(3, 6, -5))   

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q - 2 
def sum(numbers):
     total =0 
    