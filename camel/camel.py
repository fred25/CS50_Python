text = input("camelCase: ")

print("snake_case: ", end="")

for i in text:
    if i.isupper():
        print("_", end="")
    print(i.lower(), end="")

print()