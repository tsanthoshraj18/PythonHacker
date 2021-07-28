def rep():
    string = input("Enter the string:")
    k = int(input("Enter the k value"))
    while string:
        s = string[0:k]
        seen = ''
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:]
rep()