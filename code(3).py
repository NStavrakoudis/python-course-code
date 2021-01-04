""" This program creates an empty list, 
asks 3 times for the user to append a number to
the list, and finally removes the lowest one."""

a_list = []

a_list.append(int(input("Enter a number: ")))
a_list.append(int(input("Enter another number: ")))
a_list.append(int(input("Enter a third number: ")))

a_list.remove(min(a_list))
print("The list without the lowest number is: "+str(a_list))