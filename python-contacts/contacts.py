import sys

# Variable definitions
contacts = dict({})
id = 0

# Intro print
print("Name your squad")

# Main loop 
while 1:
    f = open("contacts.json", "r")
    print(f.read())
    print("Enter name or type exit")
    name = input("")
    if name == "exit":
        f = open("contacts.json", "w")
        f.write(str(contacts))
        f.close()
        sys.exit()
    print("Enter position")
    position = input("")
    print("Enter number")
    number = input("")
    id = id + 1
    contacts[id] = [name,position,number]

    print(contacts)