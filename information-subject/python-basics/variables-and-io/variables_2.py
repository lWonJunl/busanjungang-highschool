Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n1=[1,5,10]
print(n1)
[1, 5, 10]
type(n1)
<class 'list'>
n2=[1,'a',3>1]
pinrt(n2)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    pinrt(n2)
NameError: name 'pinrt' is not defined. Did you mean: 'print'?
print(n2)
[1, 'a', True]
s="hello world"
s[4]
'o'
print(s)
hello world
s
'hello world'
s[0:5]
'hello'
s[6:]
'world'
s[:4]
'hell'
s[-1]
'd'
s[-2]
'l'
n=[90,30,80,78]
print(n)
[90, 30, 80, 78]
n[1]=85
print(n)
[90, 85, 80, 78]
n[3]='one'
print(n)
[90, 85, 80, 'one']
n[0]=n[1]+n[2]
print(n)
[165, 85, 80, 'one']
m=['A','B','C','D','E']
print(m)
['A', 'B', 'C', 'D', 'E']
print(m[0]+m[1])
AB
print(m[0]*3)
AAA
print(m*3)
['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
a=[10,20,30]
b=[40,50,60]
print(a+b)
[10, 20, 30, 40, 50, 60]
c=a+b
print(c)
[10, 20, 30, 40, 50, 60]
c[0]=1
pirnt(c)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    pirnt(c)
NameError: name 'pirnt' is not defined. Did you mean: 'print'?
print(c)
[1, 20, 30, 40, 50, 60]
c[1:3]=['x','y']
print(c)
[1, 'x', 'y', 40, 50, 60]
c[1:3]=[]
print(c)
[1, 40, 50, 60]
del c[2]
print(c)
[1, 40, 60]
del c[0:2]
print(c)
[60]
tp=('red'.'green','blue')
SyntaxError: invalid syntax
tp=('red','green','blue')
type(tp)
<class 'tuple'>
print(tp)
('red', 'green', 'blue')
tp[0]
'red'
del tp[0]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    del tp[0]
TypeError: 'tuple' object doesn't support item deletion
std_tel={"홍길동":"444-1234","박정보":"123-1234"}
type(std_tel)
<class 'dict'>
print(std_tell['홍길동'])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(std_tell['홍길동'])
NameError: name 'std_tell' is not defined. Did you mean: 'std_tel'?
print(std_tel['홍길동'])
444-1234
print(std_tel['중앙고'])
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(std_tel['중앙고'])
KeyError: '중앙고'
p={7,17,3,5,7}
type(p)
<class 'set'>
print(p)
{17, 3, 5, 7}
x,y,z=1,2,3
x
1
z
3
y
2
x,y,z
(1, 2, 3)
x=y=z=10
x,y,z
(10, 10, 10)
