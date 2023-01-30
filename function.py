def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
#a=int(input("nhap a: "))
#b=int(input("nhap b: "))
a=3
b=4
x=6
y=5
print_max(a, b)
#x=int(input("nhap x: "))
#y=int(input("nhap y: "))
print_max(x, y)

#2
x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)

#3

def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)

#4
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

#5
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))