
"""Запрет наследования"""
# class Parent:
#     pass
#
#
# class Child(Parent):
#     pass
from typing import final

@final
class Parent:
    pass


class Child(Parent):
    pass


