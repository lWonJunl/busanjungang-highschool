from turtle import *

def flower(r,c):
  begin_fill()
  color(c)
  for i in range(6):
    circle(r,220)
    left(200)
  end_fill()

r=int(input("반지름:")); c=input("색상:")
flower(r,c)

