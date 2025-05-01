first_name = input("What is your name: ")
current_age = int(input("What is your age: "))
if current_age > 18:
 print("You're too old")
if current_age < 5:
 print("You are too young")
else:
 print("You are able to go")
print("Activity")
print("1.Cultural immersion. This is for 5 days and is considered “easy” and costs $800. ")
print("2.Kayaking and pancakes. This is for 3 days and is considered “moderate” and costs $ 400. ")
print("3.Mountain biking. This is for 4 days and is considered “difficult” and costs $900. ")
place = input("Choose your activity: ")
if place == "1":
 print(f"{first_name} age {current_age} has chosen Cultural immersion.")
if place == "2":
 print(f"{first_name} age {current_age} has chosen Kayaking and pancakes.")
if place == "3":
 print(f"{first_name} age {current_age} has chosen mountain biking.")