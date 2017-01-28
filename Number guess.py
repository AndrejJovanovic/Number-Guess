print ("==============================DICE=================================")
name = input("Enter your name traveller: ")
print ("Hello "+name+". Welcome to the trilling game of dice. Think of a number between 1 to 10 if you dare!!!!")
currNumber = 5
lowNumber = 1
highNumber = 11
guessOption = "no"
while (guessOption != "yes"):
	print ("Is your number higher, lower or maybe %(currNumber)d traveller" % {"currNumber": currNumber})
	guessOption = input("Write h for higher, l for lower and yes for guess: ")
	if (guessOption == "h"):
		lowNumber = currNumber
		currNumber = (lowNumber + highNumber) /2
	elif (guessOption == "l"):
		highNumber = currNumber
		currNumber = (highNumber + lowNumber) /2
	elif (guessOption == "yes"):
		print ("I showed you no mercy "+name)
	else:
		print ("Ya' try'n to make monkey out of me?")
print ("Goodbye traveller. See you on some other quest")