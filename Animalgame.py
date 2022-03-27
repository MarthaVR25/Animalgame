

print("Welcome to the animal art game")
print("Please select an animal")

def menu():
	print("[1] elephant", "\U0001f418")
	print("[2] hippo", "\U0001f99b")
	print("[0] Exit")

menu()
option = int(input("Please select an animal:"))

while option != 0:
	if option == 1:
		
		print("""
  .--()°'.'
'|, . ,'
 !_-(_\
  """)


	elif option == 2:
		
		print("""
         c~~p ,---------. 
 ,---'oo  )           \
( O O                  )/
 `=^='                 /
       \    ,     .   /
       \\  |-----'|  /
       ||__|    |_|__|"""
       )

	else:
		print("Invalid option.")

	print()
	menu()
	option = int(input("Enter an option: "))

print("Thanks for play with us")
