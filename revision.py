
# 1a) Create a class Vehicle with the following attributes:name, max_speed,mileage. Define attribute color to be “White” for all the vehicles.
#  Create two instances to confirm it works.


class Vehicle:
    color="White"
    def __init__(self, name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


        # b) Create a method that congratulates the owner  for buying that kind of a car. Include the car’s name, color,max_speed,mileage.
       
    def congratulate (self):
        return f"Hello! thank you for buying a {self.color} {self.name} with maximum speed of  {self.max_speed} kilometers per hour with a mileage of {self.mileage}"


# c)Create a method that returns the car name and its capacity.
    def name_capacity (self,capacity):

        return f"Your is car called {self.name}  and can Hold a capacity of {capacity} people"




# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

while True:
    mark = int(input("Enter the grade: "))
    if  mark <=25:
        print("F")
    elif mark >=25 and mark <=45:
        print("E")
    elif mark >=45 and mark <=50:
        print("D")
    elif mark >=50 and mark <=60:
        print("C")
    elif mark >=60 and mark <=80:
        print("B")
    else:
        mark >=80
        print("A")


# write a program that accept numbers from 1 to 7 and displays the name of the day

while True:
    number = int(input("Enter any number:"))
    if number==1:
        print("It's Monday!")
    elif number==2:
        print("It's Tuesday!")
    elif number==3:
        print("It's Wednesday!")
    elif number==4:
        print("It's Thursday")
    elif number==5:
        print("It,s Friday!")
    elif number==6:
        print("It,s Saturday!")
    else:
        number==7
        print("It's Sunday!")
def details():
 arrange={"Gumato":29, "Roba":14, "Saido":43 }

        x=list(arrange.items())
    sorted(arrange.items())

    print(dict(arrange))
    
details() 
