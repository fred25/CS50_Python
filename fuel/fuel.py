while True:
    try:
        num, den = map(int, input("Fraction: ").split("/"))
        fuel = num//den*100
    except ValueError:
        pass
    except  ZeroDivisionError:
        pass
    else:
        fuel = num//den*100
        if fuel >= 99:
            print("F")
        elif fuel <= 1:
            print("E")
        else: 
            print(f"{num/den*100}%")
        break
    