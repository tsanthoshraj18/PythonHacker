n = int(input())
if 1 <= n <= 100:
    if n % 2 or 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Enter valid Input")
