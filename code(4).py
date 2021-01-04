""" This program gets a number from the user, and then prints if
it is lower than 100, greater or equal. """

number = int(input("Enter a number: "))

if number > 100:
    print("Number is greater than 100.")
elif number == 100:
    print("Number is 100.")
else:
    print("Number is lower than 100.")