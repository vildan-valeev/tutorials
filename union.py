# from typing import Union
# from typeguard import check_argument_types, typechecked
#
# def check_and_do_stuff(a: Union[str, int]) -> None:
#     check_argument_types()
#     # do stuff ...
#
# @typechecked
# def check_decorator(a: Union[str, int]) -> None:
#     pass
#     # do stuff ...
#
# check_and_do_stuff("hello")
# check_and_do_stuff(42)
# check_and_do_stuff(3.14)  # raises TypeError