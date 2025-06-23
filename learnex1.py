#number_of_noodles = int(input("Enter number of noodles"))
  #total_noodles= int(input("Enter total noodles"))
#percent_of_noodles = (number_of_chauchau/total_noodles)*100
#print(f"The percent of noodles you have is {percent_of_noodles}%.")

msg='Welcome to Python 101: Strings'
#From this string,extract and print' Welcome 1 RIng To Tyler':Exactly 
#ANSWER
txt=msg[25:29:1]
x=txt.capitalize()

txt2 =msg[8:10]
y=txt2.capitalize()

txt3= f"{msg[13:11:-1]}{msg[2:0:-1]}{msg[25:24:-1]}"
z=txt3.capitalize()

print(f"{msg[18]} {msg[:8]} {x} {y} {z}")
  