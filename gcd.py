m = int(input())
n = int(input())
cf = 0
for i in range(min(m, n) + 1):
    if(i>0):
        if (m % i == 0) and (n % i == 0) :
            cf = i
print(cf)
