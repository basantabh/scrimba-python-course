#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
#1 ANS
if(('Eric'  in friends) and ('John'  in friends)): 
    print(f"#1 Yes they're both in the 'friends' list")
else:
    print("#1 No they're both in the 'friends' list")
#2 ANS
all_friends=friends.union(my_friends)
print(f"#2 both sets combined are {all_friends}")
#3 ANS
print(f"#3 Names present in both sets are {friends.intersection(my_friends)}")
#4 ANS
only_in_friends = friends.difference(my_friends)
print(f"#4 names only in friends are {only_in_friends}")

#5 ANS
only_in_one = friends.symmetric_difference(my_friends)
print(f"#5 names only in one of the lists are {only_in_one}")

#6 ANS
unique_cars = set(cars)
print(f"#6 {unique_cars} is the list without duplicates.")

