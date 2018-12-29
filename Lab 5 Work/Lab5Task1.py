Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> s1 ="this is a string"
>>> s2 ="this is a string"
>>> s3 = s1
>>> print(s1==s3)
True
>>> s1="aha"
>>> print(s3==s1)
False
>>> print(s3==s2)
True
>>> 
