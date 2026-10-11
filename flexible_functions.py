def print_args(*args):
    for arg in args:
        print(arg)

def add(*args):
    return sum(args)

def print_values(**kwargs):
    for key, value in kwargs.items():
        print(key, ': ', value)

print_args(1,2,3,4,"abc",True, False,None,100, "skdjh")

print(1,2,3,4,"abc",True, False,None,100, "skdjh")
print(add(1,2,3,4))

print_values(name="jackie", age=36, email='jackie@gamil.com')
