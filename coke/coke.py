money = 0
while money < 50:
    print("Amount Due:", 50-money)
    x = int(input("Insert Coin: "))
    match x:
        case 5 | 10 | 25:
            money += x

print("Change Owed:", money-50)