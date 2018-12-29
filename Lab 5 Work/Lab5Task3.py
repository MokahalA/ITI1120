Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> s5=[2, 4, "oaxaca", True]
>>> s6=[2, 4, "oaxaca", True]
>>> print(s5==s6)
True
>>> s7=s6
>>> print(s6 is s7)
True
>>> s7[3]=False
>>> print(s5)
[2, 4, 'oaxaca', True]
>>> print(s6)
[2, 4, 'oaxaca', False]
>>> print(s7)
[2, 4, 'oaxaca', False]
>>> 
