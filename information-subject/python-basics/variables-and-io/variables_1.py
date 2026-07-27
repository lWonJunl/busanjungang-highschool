Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> py_score=90
>>> type(py_score)
<class 'int'>
>>> a=-10
>>> type(a)
<class 'int'>
>>> a=0
>>> type(a)
<class 'int'>
>>> a=10
>>> a=10.0
>>> type(a)
<class 'float'>
>>> a=-10.0
>>> type(a)
<class 'float'>
>>> A=0.
>>> a=0.0
>>> type(a)
<class 'float'>
>>> <class 'float'>
SyntaxError: invalid syntax
>>> 

_py
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    _py
NameError: name '_py' is not defined
_py=100
py-s=90
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
type s=10
SyntaxError: invalid syntax
math1=90
1math=90
SyntaxError: invalid decimal literal
학생수=23
print(학생수)
23
del 학생수
print(학생수)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(학생수)
NameError: name '학생수' is not defined
100.
100.0
a-10
-10.0
a=10.
a=10.0
a=True
type(a)
<class 'bool'>
help(a)

name=중앙고
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    name=중앙고
NameError: name '중앙고' is not defined
name="중앙고"
print(name)
중앙고
type(name)
<class 'str'>
<class 'str'>
SyntaxError: invalid syntax
myAge=17.
myAge=17
myage=17
city="Busan, Korea"
print(city)
Busan, Korea
type(city)
<class 'str'>
a="Hello world"
print(a)
Hello world
print(a,sep="\n")
Hello world
a="Hello
SyntaxError: unterminated string literal (detected at line 1)
a="Hello\nworld"
print(a)
Hello
world
a="Hello\tworld"
print(a)
Hello	world
a=""Hello world""
SyntaxError: invalid syntax
a="'Hello world'"
a="Hello\"world\""
print(a)
Hello"world"
a="Hello 'world'"
print(a)
Hello 'world'
a='Hello "world"'
print9a)
SyntaxError: unmatched ')'
print9a)
SyntaxError: unmatched ')'
print(a)
Hello "world"
A="Hello"
B="turtle!"
A+B
'Helloturtle!'
A*B
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    A*B
TypeError: can't multiply sequence by non-int of type 'str'
A-B
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    A-B
TypeError: unsupported operand type(s) for -: 'str' and 'str'
A/B
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    A/B
TypeError: unsupported operand type(s) for /: 'str' and 'str'
A*5
'HelloHelloHelloHelloHello'
