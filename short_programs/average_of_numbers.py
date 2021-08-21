# Program to sum up exams score
print("Welcome to a program that can calculate average of scores")
#Variable to store total Numbers Of Subjects
den = int(input("Enter Total Numbers Of Subjects = "))
#varible to store range value
rangeVal = int(input("Enter range value = "))

#loop to iterate the number of entered values from user
vals = []
for i in range(rangeVal):
    vals.append(int(input("Enter your scores")))

#function to perform calculation of average scores
def average(vals):
    sm = sum(vals[0:len(vals)])
    print("Your Average =", sm/den)

average(vals)