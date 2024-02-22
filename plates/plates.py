def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str) -> bool:
    
    if len(s) > 6 or len(s) < 2:
        return False
    
    if not s[:2].isalpha() and not s.isalnum(): 
        return False
    
    num = False
    for i in s:
        if not num:
            if i.isnumeric():
                num = True
                if i == "0": return False
        elif not i.isnumeric():
            return False
    
    return True

main()
