MON = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        inp = input("Date: ")
        
        if "/" in inp:
            data = inp.split("/")
            if int(data[1]) > 30 or int(data[0]) > 12:
                continue
            print(f"{int(data[2]):04}-{int(data[0]):02}-{int(data[1]):02}")
            break
        data = inp.split()
        if int(data[1].replace(",", "")) > 30:
            continue
        print(f"{int(data[2]):04}-{MON.index(data[0])+1:02}-{int(data[1].replace(',', '')):02}")
        break
    except EOFError:
        break
    except IndexError:
        pass
    except ValueError:
        pass