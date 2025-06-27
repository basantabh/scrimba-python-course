
def greeting(name="someone", age=20 , fav_color="yellow", bday="May_5th"):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print(f'Hello {name.title()}, you will be {age+1} years old on {bday}! ')
    #1
    print(f"I hear you like the color {fav_color.lower()}!")
name = input('Please Enter your name: ')
age = int(input('Input your age: '))
#1
fav_color=input('What is your favourite color?')
#4
bday=input("When is your birthday?")
greeting()

# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 

#ANOTHER
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 

def greeting(name="bas", age=20 , color="red"):
    print(f"Hello {name.title()}! you will be {age+1} years old on your next birthday.")
    print(f" We hear you like the color {color.lower()}.")
name=input("Enter your name:")
age=int(input("Enter your age:"))
color=input("Enter your favourite color")
greeting(name, age, color)

