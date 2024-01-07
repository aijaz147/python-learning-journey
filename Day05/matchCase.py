number = 15
match number:
    case _ if number > 10 and number < 20:
        print("Hello World")
    case 4:
        print("Number is 4")
    case _:
        print("Not Matched")