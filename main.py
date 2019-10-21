print("hello world")

name = input("What's your name? ")

print(f"Hello {name}")


age = int(input("What is your age? "))

if age >= 18:
	print("You are an adult.")
elif age >= 13:
	print('Your are a teenager.')
else:
	print("You are a child.")