grocery_list = {}

while True:
    try:
        item = input()
        grocery_list[item] += 1
    
    except EOFError:
        print()
        for key, value in grocery_list.items():
            print(value, key.upper())
        break
    
    except KeyError:
        grocery_list[item] = 1