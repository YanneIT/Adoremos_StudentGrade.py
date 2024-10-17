"""
calculate the student's final grade
display the grade points based on the table provided:

computation of the final grade must be followed

grade input must be between the range of 40-100. otherwise, display "Invalid Grade

must be 2 decimal points

final grade must be rounded off to the nearest whole number
"""
name=input("Enter your name: ")
section=input("Enter your section: ")

prelim=float(input("Enter Prelim Grade: "))
midterm=float(input("Enter Midterm Grade: "))
finals=float(input("Enter Final Grade: "))

"""
prelim= 33.33%
midterms=33.33%
finals=33.33%
"""
"""
percentage of grades
99-100%= 1.00 Excellent
96-98%=1.25 
93-95%=1.50
90-92%=1.75
87-89%=2.00
84-86%=2.25
81-83%=2.50
78-80%=2.75
75-77%=3.00
below 75=5.00 Failed

grade range= 40-100
"""

# Check and validate prelim grade
if prelim < 40 or prelim > 100:
    print("Invalid Grade for Prelim")
else:
    print(f"Grade for Prelim: {prelim:.2f}")

# Check and validate midterm grade
if midterm < 40 or midterm > 100:
    print("Invalid Grade for Midterm")
else:
    print(f"Grade for Midterm: {midterm:.2f}")

# Check and validate finals grade
if finals < 40 or finals > 100:
    print("Invalid Grade for Finals")
else:
    print(f"Grade for Finals: {finals:.2f}")

# Calculate total grade only if all grades are valid
if (40 <= prelim <= 100) and (40 <= midterm <= 100) and (40 <= finals <= 100):
    grae = round((prelim * 0.33) + (midterm * 0.33) + (finals * 0.33))
    print(f"Total Grade: {grae}")

    # Display the grade points
    if 99 <= grae <= 100:
        print("Grade Points: 1.00 Excellent")
    elif 96 <= grae <= 98:
        print("Grade Points: 1.25 Outstanding")
    elif 93 <= grae <= 95:
        print("Grade Points: 1.50 Superior")
    elif 90 <= grae <= 92:
        print("Grade Points: 1.75 Very Good")
    elif 87 <= grae <= 89:
        print("Grade Points: 2.00 Good")
    elif 84 <= grae <= 86:
        print("Grade Points: 2.25 Satisfactory")
    elif 81 <= grae <= 83:
        print("Grade Points: 2.50 Fairly Satisfactory")
    elif 78 <= grae <= 80:
        print("Grade Points: 2.75 Fair")
    elif 75 <= grae <= 77:
        print("Grade Points: 3.00 Passed")
    else:
        print("Grade Points: 5.00 Failed")
else:
    print("Error calculating total grade.")
    
    
    
    

