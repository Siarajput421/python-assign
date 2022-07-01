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
def myint(str,n):
     result = ""
     for i in range(n):
        result= result+str
     return result
print(myint("Anu",2))
print(myint("Radha",3))

# #21.program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
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

# 22.
# 23.

# #24.program to test whether a passed letter is a vowel or not
#  n=input("enter word")
#  list=['a','i','e','o','u']
#  if n in list:
#     print("yes it,s a vowel")
#  else:
#     print("not")