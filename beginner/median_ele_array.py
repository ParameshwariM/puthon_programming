num=int(input(""))
list=[]
for i in range (num):
  list.append(int(input()))
  a=sorted(list)
  
mid=int(len(a))/2
print (a[mid])
