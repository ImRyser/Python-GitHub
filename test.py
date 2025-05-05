first_name = input("What is your name: ")
current_age = int(input("What is your age: "))
if current_age >= 18:
 print("You're too old")

elif current_age <= 5:
 print("You are too young")

else:
 print("You are able to go")
 print("Activity")
 print("1. Cultural immersion. This is for 5 days and is considered “easy” and costs $800. ")
 print("2. Kayaking and pancakes. This is for 3 days and is considered “moderate” and costs $ 400. ")
 print("3. Mountain biking. This is for 4 days and is considered “difficult” and costs $900. ")
 place = input("Choose the number of your activity: ")
if place == 1:
    print("You have chosen cultural immersion")
elif place == 2:
    print("You have chosen kayaking and pancakes")
else:
    print("you have chosen mountain biking")

transport = input("Do you need transport? (cost is $80)")
if transport == "yes":
    print("$80 has been added to your cost")
else:
    print("We will see you there!")
