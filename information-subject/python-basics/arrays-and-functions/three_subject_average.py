def avg(m,s,c):
  return (m+s+c)/3

mat=int(input("수학:"))
sci=int(input("과학:"))
cs=int(input("정보:"))
print("평균: %.2f"%avg(mat,sci,cs))
