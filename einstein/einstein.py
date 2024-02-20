def main():
    print(einstein(input("m:")))

def einstein(m:int) -> str:
    return f"E: {int(m)*300000000**2}"

main()
