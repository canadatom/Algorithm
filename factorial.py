#!/usr/bin/python

def fact(n):
    if n == 0:
        return 1
    else:
      return n * fact(n - 1)

print fact(1)
print fact(2)
print fact(5)
