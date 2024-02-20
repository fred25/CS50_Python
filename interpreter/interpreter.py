x, y, z = input("Expression: ").strip().split()

x, z = map(float, (x, z))

match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "*":
        print(x*z)
    case "/":
        print(x/z)