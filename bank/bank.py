x = input("Greeting: ").lower()

money = 100
if x.startswith("hello"):
    money = 0
elif x.startswith("h"):
    money = 20
print("$"+str(money))