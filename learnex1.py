#number_of_chauchau = int(input("Enter number of chauchau "))
  #total_chauchau = int(input("Enter total chauchau "))
#percent_of_chauchau = (number_of_chauchau/total_chauchau)*100
#print(f"The percent of chauchau you have is {percent_of_chauchau}%.")

msg='Welcome to Python 101: Strings'

txt=msg[25:29:1]
x=txt.capitalize()

txt2 =msg[8:10]
y=txt2.capitalize()

txt3= f"{msg[13:11:-1]}{msg[2:0:-1]}{msg[25:24:-1]}"
z=txt3.capitalize()

print(f"{msg[18]} {msg[:8]} {x} {y} {z}")
  