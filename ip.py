import socket
while True:
	print("Want to get IP Address ? (y/n): ")
	check = input()
	if check == 'n':
		break
	else:
		print("Your IP Address is: ",end="")
		print(socket.gethostbyname(socket.gethostname()))
		print()




import datetime
while True:
	print("Want to print Today's Date and Time ? (y/n): ")
	check = input()
	if check == 'n':
		break
	else:
		print("Today's date and time:")
		print(datetime.datetime.today())
		print()		