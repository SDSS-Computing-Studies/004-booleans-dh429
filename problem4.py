#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math

sidea = input("Enter one side:")
sidea = float(sidea)

sideb = input("Enter a second side:")
sideb = float(sideb)

sidec = input("Ener third side:")
sidec = float(sidec)

if sidea > sideb and sidea > sidec:
    hyp = sidea
    if sideb**2 + sidec**2 == hyp**2:
        print("that is a right triangle")
    elif sideb**2 + sidec**2 > hyp**2:
        print("that is an acute triangle")
    elif sideb**2 + sidec**2 < hyp**2:
        print("thas is an obtuse triangle")        

if sideb > sidea and sideb > sidec:
    hyp = sideb
    if sidea**2 + sidec**2 == hyp**2:
        print("that is a right triangle")
    elif sidea**2 + sidec**2 > hyp**2:
        print("that is an acute triangle")
    elif sidea**2 + sidec**2 < hyp**2:
        print("thas is an obtuse triangle")        

if sidec > sideb and sidec > sidea:
    hyp = sidec
    if sidea**2 + sideb**2 == hyp**2:
        print("that is a right triangle")
    elif sidea**2 + sideb**2 > hyp**2:
        print("that is an acute triangle")
    elif sidea**2 + sideb**2 < hyp**2:
        print("thas is an obtuse triangle")        