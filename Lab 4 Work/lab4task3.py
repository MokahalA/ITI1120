Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> s = '''It was the best of times, it was the worst of times;it was the age of wisdom, it was the age of foolishness;it was the epoch of belief, it was the epoch of incredulity;it was ...'''
>>> newS= s.replace(";"," ")
>>> newS=newS.replace(","," ")
>>> newS=newS.replace("\n"," ")
>>> newS=newS.replace("."," ")
>>> newS
'It was the best of times  it was the worst of times  it was the age of wisdom  it was the age of foolishness  it was the epoch of belief  it was the epoch of incredulity  it was    '
>>> newS=newS.strip()
>>> newS
'It was the best of times  it was the worst of times  it was the age of wisdom  it was the age of foolishness  it was the epoch of belief  it was the epoch of incredulity  it was'
>>> newS=newS.lower()
>>> newS
'it was the best of times  it was the worst of times  it was the age of wisdom  it was the age of foolishness  it was the epoch of belief  it was the epoch of incredulity  it was'
>>> newS.count('it was')
7
>>> newS=newS.replace("was","is")
>>> newS
'it is the best of times  it is the worst of times  it is the age of wisdom  it is the age of foolishness  it is the epoch of belief  it is the epoch of incredulity  it is'
>>> 
