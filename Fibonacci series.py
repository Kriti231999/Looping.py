Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fibonacci(i):
	if i == 0:
		return 0
	elif i == 1:
		return 1
	else:
		return fibonacci(i-2) + fibonacci(i-1)

	
>>> for x in range(13)
SyntaxError: invalid syntax
>>> for x in range(13):
	print(fibonacci(x))

	
0
1
1
2
3
5
8
13
21
34
55
89
144
>>> 