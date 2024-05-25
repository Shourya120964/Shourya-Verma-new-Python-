print("Welcom Sir".center(100 , "-"))

UserName = str(input("Pls Enter Your UserName :- "))
if (UserName == "Shourya"):
    print("Welcome Shourya")
    PassWord = input("Password :- ")
    if (PassWord == "1234",):
        print("System is Unlocked , Hi Shourya".center(180 , "."))

        def Find_Rect_Perimeter(a,b):
          Find_Perimeter=(2*(a+b))
          print("Perimeter of Rectangle :-",Find_Perimeter)

        def Find_Rect_Area(a,b):
          Find_Rect_Area = (a*b)
          print("Area of Rectangle :-",Find_Rect_Area)

        def Find_Square_Perimeter(a):
          Find_Square_Perimeter = 4*a
          print("Perimeter of Square :-",Find_Square_Perimeter)

        def Find_Square_Area(a):
          Find_Square_Area = a*a
          print("Area of Square :-",Find_Square_Area)

        def Find_Circle_Perimeter(a):
          Find_Circle_Perimeter = 2*3.14*a
          print("Perimeter of Circle :-",Find_Circle_Perimeter)

        def Find_Circle_Area(a):
          Find_Circle_Area = 3.14*a*a
          print("Area of Circle :-",Find_Circle_Area)

        def Marks_Percentage(a,b):
          Marks_Percentage = (a/b)*100
          print("Your Percentage is :-",Marks_Percentage,"%")

        print("Welcome To My Calculater".center(200, "-") , "\n")

        print("a. Perimeter of Rectangle")
        print("b. Area of Rectangle")
        print("c. Perimeter of Square")
        print("d. Area of Square")
        print("e. Perimeter of Circle")
        print("f. Area of Circle")
        print("g. Percentage of Marks")
        Choose_Options = input("Choose From Following Options :- ")
        if (Choose_Options == "a"):
          print("\nYou Choose Perimeter of Rectangle","\n")
          x = int(input("Enter Your First Number :- "))
          y = int(input("Enter Your Second Number :- "))
          Find_Rect_Perimeter(x,y)

        elif (Choose_Options =="b"):
          print("\nYou Choose Area of Rectangle","\n")
          x = int(input("Enter Your First Number :- "))
          y = int(input("Enter Your Second Number :- "))
          Find_Rect_Area(x,y)

        elif (Choose_Options =="c"):
          print("\nYou Choose Perimeter of Square","\n")
          x = int(input("Enter Your Number :- "))
          Find_Square_Perimeter(x)

        elif (Choose_Options =="d"):
          print("\nYou Choose Area of Square","\n")
          x = int(input("Enter Your Number :- "))
          Find_Square_Area(x)

        elif (Choose_Options =="e"):
          print("\n Your Choose Perimeter of Circle","\n")
          x = int(input("Enter Your Radius :- "))
          Find_Circle_Perimeter(x)

        elif (Choose_Options == "f"):
          print("\nYou Choose Area of Circle","\n")
          x = int(input("Enter Your Radius :- "))
          Find_Circle_Area(x)

        elif (Choose_Options == "g"):
          print("\nYou Choose Percentage of Marks","\n")
          x = int(input("Enter Your Marks, That you can scoored :- "))
          y = int(input("Enter Your Total Marks :- "))
          Marks_Percentage(x,y)

        else:
          print("\nYou Choose Wrong Options , This option is not available in the given options\n")

        print("Thanks For Using My Calculater".center(200, "-"))

    else:
        print("Don't Try To UnLock the System".center(180 , "."))
    
elif (UserName == "Alisha"):
       print("Welcome Mam")
       Password = input("PassWord :-")
       if(Password == "Ali.."):
          print("Your System is started")

else:
  print("......GET OUT.......")

