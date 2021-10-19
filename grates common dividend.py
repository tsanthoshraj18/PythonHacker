m = int(input())
n = int(input())
fm = []
fn = []
cf = []
for i in range(1,max(m,n)+1):

    if m % i ==0 and n % i == 0:
        cf.append(i)
print(cf[-1])
