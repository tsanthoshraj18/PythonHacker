def techgig():
    val1  = int(input())
    val2 = int(input())
    val3 = int(input())

    if val1 >= val2 and val1 >= val3:
        print(val1)
    elif val2 >= val3:
        print(val2)
    else:
        print(val3)
techgig()