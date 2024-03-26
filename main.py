#################################### Dekorator faktory metodas #####################################

# from typing import Callable

# def repeat(numb_times: int):
#     def repeat_decorator(fn: Callable):

#         def wrapper(*args, **kwargs):
#             name = fn(*args, *kwargs)
#             for _ in range(numb_times):
#                 print(f"Hello {name}")
#             return name    
#         return wrapper
#     return repeat_decorator

# @repeat(numb_times=3)
# def print_name(name: str) -> str:
#     return name

# @repeat(numb_times=5)
# def print_my_age(age: int) -> int:
#     return age

# print_name("Vilius")
# print_my_age(16)



