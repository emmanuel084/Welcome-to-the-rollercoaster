print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the roller coaster!")
  age = int(input("what is your age? "))
  if age < 12:
    bill = 5
    print("Child ticket pay $5.")
  elif age <= 18:
    bill = 7
    print("Youth ticket pay $7.")
  elif age > 19 and age < 44:
    bill = 12
    print("Adult ticket pay $12.")
  elif age >= 45 and age <=55:
    bill = 0
    print("Your ticket is free $0, enjoin it.")
  wants_photo = input("Do you want a foto taken? Type Y or N. ")
  if wants_photo == "Y" or "y":
    bill += 3 #Add $3 to their bill.
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before can ride.")