def avg(m,s,c):
  average=(m+s+c)/3
  return average

mat=int(input("수학:"))
sci=int(input("과학:"))
cs=int(input("정보:"))
result=avg(mat,sci,cs)
print("평균:",result)
