fruit = input("Item: ").lower()

cal = 0
match fruit:
    case "apple": cal = 130
    
    case "banana": cal = 110
    
    case "pear" | "sweet cherries": cal = 100
    
    case "grapes" | "kiwifruit": cal = 90
    
    case "orange" | "watermelon": cal = 80
    
    case "plums": cal = 70
    
    case "grapefruit" | "nectarine" | "peach": cal = 60
    
    case "strawberries" | "avocado" | "cantaloupe" | "honeydew melon" | "pineapple" | "tangerines": cal = 50
    
    case "lime": cal = 20
    
    case "lemon": cal = 15

if cal != 0: print("Calories:", cal)