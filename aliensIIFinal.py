#This part of the code is the initialized variables.
# This was used to set the foundation of our loop code
startAlien = int(-1)
elapsedWeeks = int(-1)
week = str("week")
alienValid = bool(False)
weekValid = bool(False)
startAlienN = str("alien")
elapsedWeeksN = str("week")

#------------------------#Explanation/user input----------------------------

#In this section we explained to the user the purpose of this program
#We then asked questions to gather information from the user
#we did this by using our initilized varibles "startAlien & elapsedWeeks"
print("This program will calculate the alien population after receiving two")
print("inputs from you; the amount of aliens that landed on earth, and how")
print("many weeks have elapsed since they landed.\n")

#-----------------------------#Calculation----------------------------------

#This section is the calculations that will determine if the user inputed a valid answer
#This would be the semi-dumby answer proof code which sends the user to the end
#if inputed a invalid answer like a negative number

#This fuction allow us to repeat a set of questions to a user until proper answer given
while alienValid == False: #Boolean which only allows 2 states 
   try: #used to catch exception
       startAlien = int(input("How many aliens landed on earth?\n"))
       if 0 <= startAlien:
           alienValid = True
           if startAlien > 1:
              startAlienN = "aliens"
           print("There were", startAlien, startAlienN, "that landed on earth.")
       else: # if anything other than valid inputs are put in
           print("Since your inputs are less than 1, mathematically the alien")
           print("population will make no sense. If you want to try the program with")
           print("numbers that are greater than 0, please run it again.")

   except ValueError: # handles exceptions 
        print("Put a whole number.")

#This function allows us to repeat a set of questions to a user until proper answer given
while weekValid == False: #Boolean which only allows 2 states
   try: #Used to catch exceptions
       elapsedWeeks = int(input("How many weeks have elapsed since they landed?\n"))
       if 1 <= elapsedWeeks:
          weekValid = True
          if elapsedWeeks > 1:
             elapsedWeeksN = "weeks"
          print(elapsedWeeks, elapsedWeeksN, "have passed.")
       else: #if anything other than valid inputs are put in
          print("Since your inputs are less than 1, mathematically the alien")
          print("population will make no sense. If you want to try the program with")
          print("numbers that are greater than 0.")
          print("")

   except ValueError: #handles exceptions
      print("")
      print("Please put a whole number.")
      print("")

#--------------------------------#forLoop--------------------------------------   

#This part of the code is the for loop in our program
# This code calculates the user input with and out puts how many aliens are on earth after x weeks
for i in range(elapsedWeeks):
    print("After", i+1, week, "there will be", startAlien * 2 ** (i+1), "aliens.")
    i+1
    if i+1 > 0:
        week = "weeks"
