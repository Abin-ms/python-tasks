# number = int(input("Enter a number : "))
# if(number>0):
#     print(number,"is positive")
# elif( number == 0):
#     print(number,"is zero")
# else:
#     print(number,"is negative")
# Take one integer and print Positive/Negative/Zero. If positive, additionally print Even/Odd using nested if.
# number = int(input())
# if( number > 0):
#     print(number,"The number is positive")
# elif( number < 0):
#     print(number,"The number is negative")
# elif( number == 0):
#     print(number,"The number is positive")
# else:
#     print("Invalid!!!!")


side1 = int(input("Enter side 1"))
side2 = int(input("Enter side 2"))
side3 = int(input("Enter side 3"))
if( (side1 + side2 > side3) & (side2 + side3 > side1) & (side3 + side1 > side2)):
    if(side1 == side2 == side3):
      print("the triangle is equilateral")
    elif((side1 == side2) | (side2 == side3) | (side1 == side3)):
      print("The triangle is isoscless")
    else:
      print("The triangle is scalen")
else:
   print("Invalid!!!1")
