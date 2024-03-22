# This program will allow the suer to calculate the circumference of the planets bellow;

import math

 

def circle(radius):# This function is calculated the circumference;

      formula = 2 * math.pi* float(radius)

      return formula

 

print ("Hello , this program will show you the circumference of the planets below !!!")

print ("\n 0)Earth \n 1)Saturn \n 2)Jupiter \n 3)Exit\n ")

 

planet = input("Please choose an option from the above options :") #input from the user;

 

while True:  #while loop is making the program to run again;

    if planet.lower() == "earth" or planet == "0":

        circumference = circle(3959)

        print ("You choice Earth and the circumference is ",circumference ," miles! ")

        planet = input("Please choose an option from the above options : ")

       

    elif planet.lower() == "saturn" or planet == "1":   

        circumference = circle(36184)

        print ("You choice Saturn and the circumference is ",circumference ," miles! ")

        planet = input("Please choose an option from the above options :")

       

    elif planet.lower() == "jupiter" or planet == "2":   

        circumference = circle(43441)

        print ("You choice Jupiter and the circumference is ",circumference ," miles! ")

        planet = input("Please choose an option from the above options :")

       

    elif planet.lower() == "exit" or planet == "3":

        break

    else:

        planet = input("Please enter a valid choice : ")


# This is tbe END of the program;
