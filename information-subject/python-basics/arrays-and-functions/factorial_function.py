def fact(n):
  global sum
  f=1
  for k in range(1,n+1):
    f*=k
  sum+=f      #sum=sum+f

sum=0
for k in range(1,6):
  fact(k)
print(sum)
