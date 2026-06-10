#                                  conditional statment in python


# age = int(input("enter your age"))

# if age >= 18 :
#     print("you can vote")
#     print("you can drive")
# else :
#     print("you can't vote")    

#                                        Traffic light

# color = input("inter the color : ")

# if color == "red":
#     print("stop")
# elif color == "green":
#     print("Go")
# elif color == "yellow":
#     print("look")
# else :
#     print("you enter invalid color")            

#                                   find the child adult and teenager 
 
# age = int(input("enter your age  :"))

# if age <= 13:
#     print("you are child")
# elif age >= 13 and age < 18:
#     print("you are teenager")     
# elif age >18 :
#     print("you are elder")
# else :
#     print("you are not a human")    

#                                simple program to login App or website 

# username = input("enter your username :")
# password = input("enter your password :")

# if (username == "admin" and password == "pass"):
#     print(" LOGIN SUCCESSFUL!")
# elif(username != "admin"):
#     print("Wrong username")
# else :
#     print("Wrong Password")     
   

#                  program to check if a number are multiple of 5 or not 

# n = int(input("enter the number"))

# if( n % 5 == 0):
#     print("Multiple of 5")
# else :
#     print("not mulltiple of 5")    


#                    print if a number is odd or even


# n = int(input("enter the number :"))

# if(n % 2 == 0 ):
#     print("Even number")
# else : 
#     print("Odd number")

#                 Nesting in conditional statment

# username = input("enter your username :")
# password = input("enter your password :")

# if (username == "admin" and password == "pass"):
#      print(" LOGIN SUCCESSFUL!")
# else :
#  if(username != "admin"):
#     print("wrong username")           
#  else :
#     print(" wrong password")   


#                 Match case in python

color = input("enter the color")

match color :
    case "green" :
        print("go")
    case "red" :
      print("stop")
    case "yellow" :
      print("look")
    case _:
      print("wrong color")          


