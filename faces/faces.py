def main():
    print(convert(input()))

def convert(text:str) -> str:
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()
