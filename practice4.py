Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l1+l2
[1, 2, 3, 4, 5, 6, 7, 8]
l3 = [l1,l2]
le
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    le
NameError: name 'le' is not defined. Did you mean: 'l1'?
l3
[[1, 2, 3, 4], [5, 6, 7, 8]]
l3 = [*l1,*l2]
l3
[1, 2, 3, 4, 5, 6, 7, 8]
names= ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
names[::-1]
SyntaxError: multiple statements found while compiling a single statement
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']
names[::-1]
['instagram', 'facebook', 'amazon', 'yahoo', 'google', 'apple']
names[2][3]
'o'
names[:2]
['apple', 'google']
names[:2] = ["unknown","unKnown"]
names
['unknown', 'unKnown', 'yahoo', 'amazon', 'facebook', 'instagram']
names[:3} = ["unknown","unKnown"]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['

b
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b
NameError: name 'b' is not defined
names[:3] = ["unknown","unKnown"]
names
['unknown', 'unKnown', 'amazon', 'facebook', 'instagram']
['unknown', 'unKnown', 'amazon', 'facebook', 'instagram']
['unknown', 'unKnown', 'amazon', 'facebook', 'instagram']
dir(names)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']
names.insert(0,10)
names
[10, 'apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']
names.pop()
'instagram'
names
[10, 'apple', 'google', 'yahoo', 'amazon', 'facebook']
names.pop(2)
'google'
names
[10, 'apple', 'yahoo', 'amazon', 'facebook']
names.remove("amezon")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    names.remove("amezon")
ValueError: list.remove(x): x not in list
names.remove("amazon")
names
[10, 'apple', 'yahoo', 'facebook']


#dictionary
d = {}
type(d)
<class 'dict'>
d = dict()
d = {"a":1,"b":2}
d = dict({"a":1,"b":2})
d =dict(a =1, b =2)
d
{'a': 1, 'b': 2}
len(d)
2
places = {"bangalore": 25, "Mysore": 35, "chennai": 30}
places["bangalore"]
25
places["h"]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    places["h"]
KeyError: 'h'
places['chennai_city']
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    places['chennai_city']
KeyError: 'chennai_city'
places.get("chennai")
30
places.get("chennai_city", 'NO Keys')
'NO Keys'
places.keys()
dict_keys(['bangalore', 'Mysore', 'chennai'])
places.values()
dict_values([25, 35, 30])
places.items()
dict_items([('bangalore', 25), ('Mysore', 35), ('chennai', 30)])
places.update({punjab = 38})
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
places.update(pinjab =38)
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'pinjab': 38}
places.setdefault("kerala")
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'pinjab': 38, 'kerala': None}
places.setdefault("kerala",10)
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'pinjab': 38, 'kerala': None}
places.setdefault(cochin = 20)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    places.setdefault(cochin = 20)
TypeError: dict.setdefault() takes no keyword arguments
places.setdefault("cochin", 20)
20
places
{'bangalore': 25, 'Mysore': 35, 'chennai': 30, 'pinjab': 38, 'kerala': None, 'cochin': 20}
l = ["a", 'b', 'c']
d = {}
d.fromkeys(l)
{'a': None, 'b': None, 'c': None}
d.fromkeys(l,True)
{'a': True, 'b': True, 'c': True}
