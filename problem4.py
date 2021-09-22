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
side1 = input("Enter one side:")
side1 = float(side1)

side2 = input("Enter a second side:")
side2 = float(side2)

side3 = input("Enter the third side:")
side3 = float(side3)

#Check if side1 is longer than side2
if side1 > side2:
    #Check if side2 is longer than side3
    if side2 >= side3:
        hyp = side1
    #If side3 is longer than side2 it checks if its longer than side3
    else:
        if side3 > side1:
            hyp = side3
        else:
            hyp = side1

    
#if side2 is longer 
elif side1 < side2:
    if side1 >= side3: 
        hyp = side2
    else:
        if side3 > side2:
            hyp = side3
        else:
            hyp = side2


if hyp == side1:
    if side2**2 + side3**2 == hyp**2:
        print("that is a right triangle")

if hyp == side2:
    if side1**2 + side3**2 == hyp**2:
        print("that is a right triangle")

if hyp == side3:
    if side1**2 + side2**2 == hyp**2:
        print("that is a right triangle")


