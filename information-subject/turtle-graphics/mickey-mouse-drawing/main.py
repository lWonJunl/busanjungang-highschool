from turtle import *
f=open("미키마우스.txt")
s=[]
for row in f.readlines():
  s.append(list(row.strip()))
penup()
for y in range(15):
  for x in range(15):
    goto(x*20,-y*20)
    if s[y][x]=="1":
      color("black")
    else:
      color("white")
    dot(20)
