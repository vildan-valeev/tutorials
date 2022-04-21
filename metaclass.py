# class MyMeta(type):
#     pass
#
#
# class MyClass(metaclass=MyMeta):
#     pass
#
#
# class MySubclass(MyClass):
#     pass
#
#
# print(type(MyMeta))
# print(type(MyClass))
# print(type(MySubclass))
#
#
# class SingletonMeta(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class SingletonClass(metaclass=SingletonMeta):
#     pass












