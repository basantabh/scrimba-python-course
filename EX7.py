print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
#ANSWER
#Function for athemetic calculator
def calculator(a, b, symbol):
    if(symbol=="/"):
        return a/b
    elif(symbol=="*"):
        return a*b
    elif(symbol=="+"):
        return a+b
    elif(symbol=="-"):
        return a-b
    else:
        return None
#Fuction for temperature calculator
def f_to_c(f):
    return None
def c_to_f(c):
    return c*9/5 + 32
#Code for calculator
mode = input("Enter mode (temp/arth)")
if(mode == "arth"):
    symbl = input("Enter mode:(/,*,+,-)")
    m=float(input("enter first number"))
    n=float(input("enter second number"))
    print(calculator(m, n, symbl))
else:
    typ = input("Select type (c_to_f)/(f_to_c)")
    temp = float(input("Enter temperature"))
    if(typ == "c_to_f"):
        print(c_to_f(temp))
    else:
        print(f_to_c(temp))