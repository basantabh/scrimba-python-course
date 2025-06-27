names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
#You are having a party and want to invite your friends.
#You want to print out invitations for each friend using for loops.
#The names are in two lists, names and names1.
#You also need to add two extra names to the list using an input box when you run the code.
#Print out one invitation to each friend per line.
#Names should be properly capitalized.
#Example of printout:
#John Cleese! You are invited to the party on saturday.
#Eric Idle! You are invited to the party on saturday.
#Hint: You may need two (for) loops to solve this exercise.

#REFRENCE:
#for i in range(1,5):
#     print(f"{i*"--"}{">"} Loops are really cool {i*"!"}")

#ANSWER:
#namez=[input("Enter one more person to invite:"),input("Enter another person to invite:")]
#all_names= names + namez
for i in all_names:
    i.lower()
    print(f"{i.title()}! You are invited to the party on saturday.")
for i in names1:
    i.lower()
    print(f"{i.title()}! You are invited to the party on saturday.")




