def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    def get_a(a, b):
        return a

    return pair(get_a)


def cdr(pair):
    def get_b(a, b):
        return b

    return pair(get_b)


print(car(cons(23, 45)))
print(cdr(cons(23, 45)))



