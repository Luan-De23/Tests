num = input("type --> ")
x = 0

for i in range (len(num)):
    x += int(num[i])

x = str(x)
if x == "9":
    print("divisible")
else:
    print("Not ")