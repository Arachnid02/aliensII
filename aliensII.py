startAlien = int(-1)
elapsedWeeks = int(-1)
week = str("week")
alienValid = bool(False)
weekValid = bool(False)

print("This program will calculate the alien population after receiving two")
print("inputs from you; the amount of aliens that landed on earth, and how")
print("many weeks have elapsed since they landed.\n")

while alienValid == False:
   try:
       startAlien = int(input("How many aliens landed on earth?\n"))
       if 0 <= startAlien:
            alienValid = True
       else:
           print("Since your inputs are less than 1, mathematically the alien")
           print("population will make no sense. If you want to try the program with")
           print("numbers that are greater than 0, please run it again.")

   except ValueError:
        print("Put a whole number.")

if elapsedWeeks <= 0:
    print("Since your inputs are less than 1, mathematically the alien")
    print("population will make no sense. If you want to try the program with")
    print("numbers that are greater than 0, please run it again.")

for i in range(elapsedWeeks):
    print("After", i+1, week, "there will be", startAlien * 2 ** (i+1), "aliens.")
    i+1
    if i+1 > 0:
        week = "weeks"
