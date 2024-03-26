# Create a decorator factory (decotator) that applies a given function to the result of the decorated function.
# Example, main function is to add 2 nubmers , but decorator factory is to return square of the nubmers. 
# example: print(add_numbers(1,2)) returns 9 .

# def decorator_factory(func):
#     def decorator(inner_func):
#         def wrapper(*args, **kwargs):
#             result = inner_func(*args, **kwargs)
#             return func(result)
#         return wrapper
#     return decorator

# # Define the decorator function that squares the result
# @decorator_factory(lambda x: x**2)
# def add_numbers(a, b):
#     return a + b

# # Test the decorated function
# result = add_numbers(1, 2)
# print(result)  # Output: 9

##################### Alberto ################################

# from typing import Callable

# def do_pow(function: Callable) -> Callable:
#     def useless_decorator(fn: Callable):
#         def wrapper(*args, **kwargs):
#             my_func = fn(*args, **kwargs)
#             return function(my_func)
#         return wrapper
#     return useless_decorator

# def raise_square(number: int) -> int:
#     return number**2

# @do_pow(function=raise_square)
# def sum_numbers(a: int, b: int) -> int:
#     return a + b

# print(sum_numbers(1, 2))

###############################################################
# Create a decorator factory logging decorator that executes decorated function n given times if function raises an error.
# When function is correctly executed , logging should log to file how many times executions failed, and the result of succesfull execution.
# Create any function that could prbably fail.

# import logging

# def logging_decorator_factory(filename, max_attempts):
#     def logging_decorator(func):
#         def wrapper(*args, **kwargs):
#             attempts = 0
#             while attempts < max_attempts:
#                 try:
#                     result = func(*args, **kwargs)
#                     with open(filename, 'a') as file:
#                         file.write(f'Successful execution. Result: {result}\n')
#                     return result
#                 except Exception as e:
#                     attempts += 1
#             with open(filename, 'a') as file:
#                 file.write(f'Failed after {max_attempts} attempts.\n')
#             return None
#         return wrapper
#     return logging_decorator

# # Define the function that could potentially fail
# @logging_decorator_factory('log.txt', 3)
# def divide(a, b):
#     return a / b

# # Test the decorated function
# result = divide(10, 2)
# print(result)  # Output: 5

# result = divide(10, 0)
# print(result)  # Output: None

######################### Mykolo ##########################################
# from typing import Callable, Union
# from random import randint
# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="data.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%d/%m/%Y %H:%M:%S",
# )


# def repeat_n_times_or_till_success(repeat_times):
#     def attempt_function(fn: Callable):
#         def wrapper(*args, **kwargs):
#             for i in range(repeat_times):
#                 try:
#                     result = fn(*args, **kwargs)
#                     logging.info(
#                         f"Function succeeded after {i+1} attempts. Result: {result}"
#                     )
#                     return result
#                 except Exception:
#                     pass

#         return wrapper

#     return attempt_function


# @repeat_n_times_or_till_success(repeat_times=7)
# def random_division(number_to_divide: Union[int, float]) -> Union[int, float]:
#     return number_to_divide / randint(0, 4)


# print(random_division(5))