sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = sales_w1 + sales_w2
sales_w2.insert(1,int("24"))
sales.sort()
sales_w1.sort()
sales_w2.sort()
print(f"{sales[-1]}$ is earned on the best day of both weeks, and {sales[0]}$ is earned on the worst. ")
print(f"{sales_w1[-1]}$ is earned on the best day of the first week, and {sales_w1[0]}$ is earned on the worst.")
print(f"{sales_w2[-1]}$ is earned on the best day of the second week, and {sales_w2[0]}$ is earned on the worst.")