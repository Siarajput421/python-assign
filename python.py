#1."Twinkle, twinkle,..... little star",
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#2.Write a Python program to get the Python version you are using
#import sys
#print(sys.version)

#3. Write a Python program to display the current date and time.
# import datetime
# n=datetime.datetime.now()
# print(n)

# 4  Write a Python program which accepts the radius of a circle from the user and compute the area.
# n=float(input("enter the value= "))
# a=3.14*(n*n)
# print(a)

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# a=("Anu")
# b=("Radha")
# print (b, " ", a)

# 6.. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# v = input("enter numbers" )
# list = v.split(",")
# tuple = tuple(list)
# print('List :',list)

# 7 Write a Python program to accept a filename from the user and print the extension of that.
# x="my.nb"
# y=x.split(".")
# print(y[-1])

# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print (color_list[0],color_list[3])

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date)
# a = (11, 12, 2014)
# print ("date: %i / %i / %i"%a)

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# print(abs.__doc__)

# 12. Write a Python program to print the calendar of a given month and year.
# import calendar
# y = int(input("input the year :"))
# m = int (input("intput the month :"))
# print(calendar.month(y,m))

# 13. Write a Python program to print the following 'here document'. 
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# print("""
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")

# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

# from datetime import date
# a= date(2014, 7, 2)
# b= date(2014, 7, 11)
# y= a-b
# print(y.days)

# 15. Write a Python program to get the volume of a sphere with radius 6.
# pi = 3.1415926535897931
# r= 6.0
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V)

#16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2 

# print(difference(23))
# print(difference(13))

#17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

# def near_thousand(n):
#       return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))   
# print(near_thousand(2200))

# 18.program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
# a=4
# b=4
# c=4
# if a==b==c:
#     print(int(a+b+c)*3)
# else:
#     print(a+b+c)

# 19.program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged
# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str

# print(new_string("Isnew"))
# print(new_string("IsOld"))

# #20.program to get a string which is n (non-negative integer) copies of a given string
# def myint(str,n):
#      result = ""
#      for i in range(n):
#         result= result+str
#      return result
# print(myint("Anu",2))
# print(myint("Radha",3))

# 21.program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
#  n=int(input("enter number"))
#  if n%2 == 0:
#      print("Even number")
#  else:
#      print("Odd")
# program to count the number 4 in a given list.
# def myfunc(num):
#     count=0
#     for i in num:
#         if i == 4:
#             count=count+1
#     return count
# print(myfunc([1,3,2,4,5,6,4,4]))

# 23.

# 24.program to test whether a passed letter is a vowel or not
#  n=input("enter word")
#  list=['a','i','e','o','u']
#  if n in list:
#     print("yes it,s a vowel")
#  else:
#     print("not")

#25. Write a Python program to check whether a specified value is contained in a group of values.
# def is_group_member(group_data, n):
#    for value in group_data:
#        if n == value:
#            return True
#    return False
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))

#26. Write a Python program to create a histogram from a given list of integers.
# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '*'
#           times = times - 1
#         print(output)
# histogram([2, 7, 5, 6])

#27. Write a Python program to concatenate all elements in a list into a string and return it
# def concatenate_list_data(list):
#     result= ''
#     for element in list:
#         result += str(element)
#     return result
# print(concatenate_list_data([4, 5, 12, 6]))

#28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence
# numbers = [
    # 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    # 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    # 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    # 958,743, 527
    # ]
    #
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# for x in numbers:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)

#29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print("Original set elements:")
# print(color_list_1)
# print(color_list_2)
# print("\nDifferenct of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))
# print("\nDifferenct of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))

#30. Write a Python program that will accept the base and height of a triangle and compute the area.
# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
# area = b*h/2
# print("area = ", area)

#33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
# def sum_three(x, y, z):
#     if x == y or y == z or x==z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
# print(sum_three(2, 1, 2))
# print(sum_three(3, 2, 2))
# print(sum_three(2, 2, 2))
# print(sum_three(1, 2, 3))

#34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum
# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))

#37. Write a Python program to display your details like name, age, address in three different lines
# def personal_details():
#     name, age = "Anu", 25
#     address = "Mohali, Chandigarh, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
# personal_details()
#38. Write a Python program to solve (x + y) * (x + y).
# x= int(input("User Input Value1: "))
# y= int(input("User Input Value2: "))
# result = x * x + 2 * x * y + y * y
# print(result)

#39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
#  amt = 10000, int = 3.5, years = 7
# amt = 10000
# int = 3.5
# years = 7
# future_value = amt*((1+(0.01*int)) ** years)
# print(round(future_value,2))

#48. Write a Python program to parse a string to Float or Integer.
# n = "348.3458"
# print(float(n))
# print(int(float(n)))

#50. Write a Python program to print without newline or space.
# for i in range(0, 10):
#     print('*', end="")
# print("\n")
