import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

#2
from math import sqrt
print("Square root of 16 is", int(sqrt(16)))

#3
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

def say_hi():
    print('Hi, this is mymodule speaking.')

__version__ = '0.1'
