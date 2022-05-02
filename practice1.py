Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help("false")
No Python documentation found for 'false'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

name = "john"
age = 32
print("my name is",name)
my name is john
print("my age is:",age)
my age is: 32
print('a' \n "b")
SyntaxError: unexpected character after line continuation character
print('a'"\n"'b')
a
b
print("a", 'b',sep="&")
a&b
string = "hi welcome to python"
string[::2]
'h ecm opto'
string[::-2]
'nhy teolwi'
string[::-1]
'nohtyp ot emoclew ih'
filename = 'youtube.txt'
filename[-3:]
'txt'
filename[:7]
'youtube'
url = 'https://google.com'
url[:5]
'https'
url[8:14]
'google'
'google'
'google'
d = {}
type(d)
<class 'dict'>

d= dict()
type(d)
<class 'dict'>
d ={"a":1,"b":2}
d = dict({"a":1,"b":2})
d= dict(a=1,b=2)
d= dict([("a",1)("b",2)])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d= dict([("a",1)("b",2)])
TypeError: 'tuple' object is not callable
type(d)

d1= dict([("a",1),("b",2)])
type(d1)
<class 'dict'>
places = {"bangalore": 25,"mysore":35,"chennai":30}
places["bangalore"]
25
places["chennai_city"]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    places["chennai_city"]
KeyError: 'chennai_city'
places.get("chennai")
30
places.get("chennai_city", "NO Key")
'NO Key'
places.keys()
dict_keys(['bangalore', 'mysore', 'chennai'])
places.values()
dict_values([25, 35, 30])
