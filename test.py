# Given list x = [100,110,120,130,140,150], use list comprehension to create another list containing each number in the list multiplied by 5.  
# def numbers():
#    listx= [100,110,120,130,140,150]
#    for b in listx:
#       if b%5==0:
#         print(b)
# numbers()  


# Write a function named divisible_by_three that accepts a number n and prints all numbers from 1 to n that are divisible by 3. 


# Given the nested list x = [[1,2],[3,4],[5,6]], write a function that flattens the list and returns it as [1,2,3,4,5,6]

# Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list. Example:
# smallest([3,6,8,2,4,1,5,7]) returns 1

# Write a function that accepts list x below and uses a set to remove the duplicate letters and returns the list without duplicates
# x = ['a','b','a','e','d','b','c','e','f','g','h']

# Write a function named divisible_by_seven that; using the range function and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.

# Given this list of students containing age and name,  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], write a function that greets each student and tells them the year they were born. e.g Hello Eunice, you were born in the year 2002.





# Create a Class Rectangle with the following Attributes and Methods
# Attributes: The class has attributes width and length that represent the two sides of a rectangle 
# Methods:
#  Add a method named area which returns the area (A) of the rectangle using the formula A=width*length
# Add a method named perimeter which returns the perimeter (P) of the rectangle using the formula P=2(length+width)


# def calculation(a,b):
#    Subtraction = a-b
#    Addition = a + b
#    return Subtraction, Addition



#    Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

   # outer function
def fun(a, b):

    # inner function
    def addition(a, b):
        return a + b

    # calling inner function from outer function
    add = addition(a, b)
    return add + 5
