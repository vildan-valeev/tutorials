class A:
    pass


class B(A):
    pass


class C:
    pass


class D(C):
    pass


class E(B, D):
    pass


def print_mro(T):
    print(*[c.__name__ for c in T.mro()], sep=' -> ')

print_mro(E)