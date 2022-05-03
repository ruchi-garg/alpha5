Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a =10
float(a)
10.0
complex(a)
(10+0j)
bool(a)
True

#float
a =12.75
int(a)
12
complex(a)
(12.75+0j)
bool(a)
True

#complex
a = 1+2j
int(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
bool(a)
True
s = "hello world"
s[0:len(s):1]
'hello world'
s[::1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s[::1]
'hello world'
s[0:5]
'hello'
s[::2]
'hlowrd'
s[::3]
'hlwl'
s =[::-1]
SyntaxError: invalid syntax
s[::-1]
'dlrow olleh'
s == s[::-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s ==s[::-1]
False
False
False
filename = "youtube.txt"
filename[7:]
'.txt'
filename[8:}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
filename[8:]
'txt'
filenname[:6]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    filenname[:6]
NameError: name 'filenname' is not defined. Did you mean: 'filename'?
filename[:6]
'youtub'
filename[:7]
'youtube'
filename[:-4]
'youtube'
url = 'https://google.com'
url[:5]
'https'
url[8:14]
'google'
s[1]
'e'
s = "hello world"
s[1]
'e'
s[1] = 'z'
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s[1] = 'z'
TypeError: 'str' object does not support item assignment
dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
s.upper()
'HELLO WORLD'
s.lower()
'hello world'
s.swapcase()
'HELLO WORLD'
s ='hello world'
s.count("o")
2
s.count("o",7)
1
s.count("o",3,10)
2
s.index("e")
1
s.index("r")
8
s.index("b")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s.index("b")
ValueError: substring not found
s.find("b")
-1
s.rindex("l")
9
s.index("l")
2
s = "hello world"
s.replace("e","z")
'hzllo world'
s.replace("o", "y")
'helly wyrld'
s.replace("o","y",1)
'helly world'
s.startswith("h")
True
s.startswith("y")
False
sentence = "python is a programming language"
sentence.split()
['python', 'is', 'a', 'programming', 'language']
s = 'hello'
"_".join(s)
'h_e_l_l_o'
"%".join(s)
'h%e%l%l%o'
sentence = "python is a programming language"
l = sentence.split()
print(l)
['python', 'is', 'a', 'programming', 'language']
"".join(l)
'pythonisaprogramminglanguage'
" ".join(l)
'python is a programming language'
s = "         hello     "
s.strip()
'hello'
s = "##############*******hai$$$@@@@@@@@@*"
s.strip("#*$@")
'hai'
