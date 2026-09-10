def func1(x):
    x = 'a' + x
    return x


def func2(y):
    y.append('c')
    return y


def func3(z):
    z['new_key'] = 'new_value'


if __name__ == '__main__':
    a = 'b'
    b = func1(a)
    print(a, b)

    c = ['d', 'e']
    d = func2(c)
    print(c, d)

    e = {'key': 'value'}
    f = func3(e)
    print(e, f)