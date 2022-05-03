Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1 = {2,4,6,8,10}
s2 = {3,6,9,12}


#union
s1.union(s2)
{2, 3, 4, 6, 8, 9, 10, 12}

#
#
s1.intersection(s2)
{6}
s1.difference(s2)
{8, 2, 10, 4}
s2.difference(s2)
set()
s2.difference(s1)
{9, 3, 12}
s1-s2
{8, 2, 10, 4}
"hai" + "hello"
'haihello'

[1,2] +[3,4]
[1, 2, 3, 4]
(1,2)+(3,4)
(1, 2, 3, 4)
s1+s2
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s1+s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
die(s1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    die(s1)
NameError: name 'die' is not defined. Did you mean: 'dir'?
dir(s1)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
s1.update(s2)
s1
{2, 3, 4, 6, 8, 9, 10, 12}
a = {"google","gmail"}
b = {"fb", "insta","google"}
a.update(b)
a
{'google', 'insta', 'gmail', 'fb'}
a.intersection_update(b)
a
{'google', 'fb', 'insta'}
a = {"google","gmail"}
b = {"fb", "insta","google"}
SyntaxError: multiple statements found while compiling a single statement
a.itersection_update(b)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.itersection_update(b)
AttributeError: 'set' object has no attribute 'itersection_update'. Did you mean: 'intersection_update'?
a = {"google","gmail"}

b = {"fb", "insta","google"}

a.intersection_update(b)
a

t1 = (1,2)
t2 = (3,4)
t1+t2
(1, 2, 3, 4)
(*t1,*t2)
(1, 2, 3, 4)
t = (1,2,3,4,["hai","hello",23],"python")

t[4]
['hai', 'hello', 23]
t[4][0]
'hai'
t[4][0][-1]
'i'
t[4][0][-1] = 'y'
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    t[4][0][-1] = 'y'
TypeError: 'str' object does not support item assignment
b = {"fb","insta","google"}
b.update("gmail")
b
{'insta', 'm', 'g', 'i', 'google', 'l', 'a', 'fb'}
b = {"fb","insta","google"}
b.add(10)
b
{'google', 10, 'fb', 'insta'}
{'google', 10, 'fb', 'insta'}
{'google', 10, 'fb', 'insta'}
b.update("gmail")
b
{'insta', 'm', 10, 'g', 'i', 'google', 'l', 'a', 'fb'}
b = {"fb","insta","google"}
b.add("gmail")
b
{'google', 'fb', 'insta', 'gmail'}
b.update(1.25)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    b.update(1.25)
TypeError: 'float' object is not iterable
b = {"fb","insta","google"}
b.pop()
'google'
b.pop()
'fb'
b.clear()
b
set()
id(b)
1924020966496
del b
id(b)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    id(b)
NameError: name 'b' is not defined
