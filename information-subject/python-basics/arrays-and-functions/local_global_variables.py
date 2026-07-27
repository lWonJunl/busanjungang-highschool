def divisorCount(n):
  tot=0
  for i in range(1,n+1):
    if n%i==0:
      tot+=1
  print("약수 개수:",tot)
  return tot
tot=0
tot+=divisorCount(10)
tot+=divisorCount(20)
print("약수 누적 개수:",tot)
