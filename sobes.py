# def f(x, y={}):
#     print(y)
#     y[x] = x
#     print(x, y)
#     print('--')
#
#
# f(1)
# f(2)
# f(3)
#
#
#
# x = [1, 2]
# y = {}
# y[x] = 1
# print(y)


# def multipliers():
#     return [lambda x: i * x for i in range(4)]
#
#
# print([m(2) for m in multipliers()])



# def multipliers():
#     return [(lambda x, i=i: i * x) for i in range(4)]
#
#
# print([m(2) for m in multipliers()])


# class A(object):
#     x = 1
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# print(A.x, B.x, C.x)
# B.x = 2
# print(A.x, B.x, C.x)
# A.x = 3
# print(A.x, B.x, C.x)


my_list = [1, 2, 5, 10]

copy_list = my_list.copy()
copy_list.extend([44, 77, 0])

print(my_list)