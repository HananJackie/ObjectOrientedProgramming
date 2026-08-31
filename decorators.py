def my_decorator(func):
    def wrapper():
        print(f'Add here actions that will occur prior executing the function {func}')
        func()
        print(f'Add here actions that will occur after executing the function {func}')
    return wrapper

def say_hello():
    print('Hello!')

say_hello = my_decorator(say_hello)

if __name__ == "__main__":
    say_hello()
    pass