
import random

comp_number = random.randint(1, 100)

while True:

	user_number = input("\nGuess the number (1-100) or q for quit: ")  

	if user_number == "q":
		print("bye bye!")
		break

	if not user_number.lstrip("-").isdigit():      
		print("Please enter the number!")
		continue

	user_number = int(user_number)

	if user_number < 1 or user_number > 100:
		print("Please enter the number between 1-100 range!")
		continue

	elif user_number == comp_number:  
		print("Number: ", comp_number,"Congratulations!")
		break

	elif user_number < comp_number:
		print("Your number is lower!")

	elif user_number > comp_number:
		print("Your number is upper!")