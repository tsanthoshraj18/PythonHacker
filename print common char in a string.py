a = int(input())
ak =[]
for i in range(0,a):
 san =input()
 ak.append(san)
mm=[]
for i in zip(*ak):
  if i.count(i[0])==len(i):
    mm.append(i[0])
  else:
    break
print(''.join(mm))    