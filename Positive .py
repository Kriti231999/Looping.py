Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Org_list = input("Enter list:"):
	
SyntaxError: invalid syntax
>>> Org_list = int (input("enter list:"))
enter list:-3,2,1,4,-5
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Org_list = int (input("enter list:"))
ValueError: invalid literal for int() with base 10: '-3,2,1,4,-5'
>>> List = [12,-7,,5,64,,-14]
SyntaxError: invalid syntax
>>> List = [12,-7,5,64,-14]
>>> for num in List:
	if num >= 0:
		print(num, end = "")

		
12564
>>> 
>>> List = [12,-7,5,,64,-14]
SyntaxError: invalid syntax
>>> List = [12,-7,5,64,-14]
>>> for num in List:
	if num >= 0:
		print(num, end = " ")

		
12 5 64 
>>> 