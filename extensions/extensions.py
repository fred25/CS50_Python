x = input("File name: ").strip().lower().split(".")[-1]

match x:
    case "gif"|"jpg"|"jpeg"|"png":
        print("image/"+x)
    case "pdf" | "zip":
        print("application/"+x)
    case "txt":
        print("text/"+x)
    case _:
        print("application/octet-stream")