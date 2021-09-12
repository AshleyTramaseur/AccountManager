
#files
accounts = open("accounts.txt", "r")
passwords = open("passwords.txt", "r")

usr_names = []
for line in accounts:
	data = line.strip()
	usr_names.append(data)

passwrds = []
for line in passwords:
	data = line.strip()
	passwrds.append(data)

accounts.close()
passwords.close()

#vars
usrnm_input = ''
pwrd_input = ''
pv1 = 0
pv2 = 0
#'pv' stands for position value
val = 0
#used to append the value of pv1 & 2 to more than the length of the lists
n = 0
x = 0
#used for the username input and verification loop
startup = ""
am = 0
nan = ""
nap = ""
apc = ""
ep = ""
np = ""
an = ""
ap = ""
yn = ""

def update_files():
  accounts = open("accounts.txt", "w")
  passwords = open("passwords.txt", "w")
  for element in usr_names:
    accounts.write(element + "\n")
  for element in passwrds:
    passwords.write(element + "\n")
  accounts.close()
  passwords.close()

print('~~~~~{STARTUP}~~~~~')

#main program
while True:
  update_files()
  print("[1] Check login | [2] Manage accounts ")
  startup = input(": ")
  startup = int(startup)
  n = 0
  x = 0
  
  if startup == 1:
  	#adjusting the value of pv1 and 2 to stop false verification
  	val = len(usr_names)
  	pv1 = val
  	pv2 = val + 1
  	#print("pv1: ", pv1)
  	#print("pv2: ", pv2)
  
  	while n <= 1:
  		usrnm_input = input('Enter Username: ')
  		if usrnm_input in usr_names:
  			pv1 = usr_names.index(usrnm_input)
  			n = 2
  		else:
  			print("Incorrect username. ")
  	while x <= 1:
  		pwrd_input = input('Enter Password: ')
  		if pwrd_input in passwrds:
  			pv2 = passwrds.index(pwrd_input)
  			x = 2
  		else:
  			print("Incorrect password. ")
  
  	#print("pv1: ", pv1)
  	#print("pv2: ", pv2)
  
  	if pv1 == pv2:
  		print("Login successful. ")
  	else:
  		print("Username and password does not match. ")
  
  elif startup == 2:
  	print("[1] Add account | [2] Change password | [3] Remove account ")
  	am = input(": ")
  	am = int(am)
  	if am == 1:
  		print("Enter new account name")
  		nan = input(": ")
  		print("Enter new account password")
  		nap = input(": ")
  		usr_names.append(nan)
  		passwrds.append(nap)
  		print("Account succesfully added")
  	elif am == 2:
  		while n <= 1:
  			print("What account would you like to change the password for?")
  			apc = input(": ")
  			if apc in usr_names:
  				pv1 = usr_names.index(apc)
  				print("Enter existing password")
  				ep = input(": ")
  				pv2 = passwrds.index(ep)
  				if pv1 == pv2:
  					print("Enter new password")
  					np = input(": ")
  					passwrds[pv2] = np
  					print("Change password successful")
  					n = 3
  				else:
  					print("Incorrect password")
  					n = n + 1
  			elif apc == "cancel":
  			  n = 3
  			else:
  				print("Account does not exist")
  
  	elif am == 3:
  		print("Account you would like to remove")
  		an = input(": ")
  		if an in usr_names:
  			pv1 = usr_names.index(an)
  			print("Account password")
  			ap = input(": ")
  			pv2 = passwrds.index(ap)
  			if pv1 == pv2:
  				print("Are you sure you would like to remove this account?")
  				yn = input(": ")
  				yn = yn.lower()
  				if yn == "yes":
  					print("Account removed successfully")
  					n = 3
  					usr_names.pop(pv1)
  					passwrds.pop(pv2)
  				else:
  					print("Action cancelled")
  					n = 3
  			else:
  				print("Incorrect password")
  				n = n + 1
  		else:
  			print("Account does not exist")
  	else:
  		print("Command not recognised")
  
