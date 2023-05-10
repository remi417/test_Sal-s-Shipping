Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Sal's Shipping
... weight = 1.5
... 
... # ground shipping
... if weight <= 2.0:
...   print(weight*1.5+20)
... elif weight <= 6.0:
...   print(weight*3+20)
... elif weight <=10:
...   print(weight*4+20)
... else:
...   print(weight*4.75+20)
... 
... # ground shipping premium
... gsp = 125.00
... print(gsp)
... 
... # drone shipping
... if weight <= 2.0:
...   print(weight*4.5)
... elif weight <= 6.0:
...   print(weight*9)
... elif weight <=10:
...   print(weight*12)
... else:
