"""
This module provides functions to read a file, check if a target number can be
achieved using a combination of operations, and measure the execution time of
functions. It includes a main function to sum keys for which a target can be
achieved using specified operations.
"""
import time
from functools import wraps
from math import log10


def timeit(func: callable) -> callable:
    """
    A decorator that measures the execution time of a function.

    Args:
        func (callable): The function to be measured.

    Returns:
        callable: The wrapped function with added timing functionality.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function '{func.__name__}': {(end - start):.6f} seconds")
        return result
    return wrapper


def read_file(pathname: str) -> list[tuple[int, tuple[int]]]:
    """
    Reads a file and returns its content as a list of tuples.

    Each line in the file is read and split into a key and a tuple of values.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        list[tuple[int, tuple[int]]]: A list of tuples, each containing an
        integer key and a tuple of integer values.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return [(int(key), tuple(map(int, values.split())))
                for key, values in (line.strip().split(':') for line in file)]


def is_possible(key: int, values: tuple[int], symbols: tuple[str]) -> bool:
    """
    Determines if a target key can be achieved using a combination
    of operations on a tuple of values.

    Args:
        key (int): The target number to be achieved.
        values (tuple[int]): A tuple of integers to be combined using
        operations.
        symbols (tuple[str]): A tuple of operation symbols ('+', '*', '||').

    Returns:
        bool: True if the target key can be achieved, False otherwise.
    """
    possible_results = [set() for _ in range(len(values))]
    possible_results[0].add(values[0])
    new_res = 0

    for i, val in enumerate(values[1:], start=1):
        for prev_result in possible_results[i-1]:
            for op in symbols:
                if op == '+':
                    new_res = prev_result + val
                elif op == '*':
                    new_res = prev_result * val
                elif op == '||':
                    new_res = prev_result * 10**(int(log10(val)) + 1) + val

                if new_res <= key:
                    possible_results[i].add(new_res)

    return key in possible_results[-1]


@timeit
def main_function(dct: list[tuple[int, tuple[int]]],
                  symbols: tuple[str]) -> int:
    """
    Sums the keys for which the target can be achieved using specified
    operations.

    Args:
        dct (list[tuple[int, tuple[int]]]): A list of tuples containing keys
        and values.
        symbols (tuple[str]): A tuple of operation symbols ('+', '*', '||').

    Returns:
        int: The sum of keys for which the target can be achieved.
    """
    return sum(key for key, values in dct if is_possible(key, values, symbols))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 7/test.txt')
    input_real = read_file('Day 7/input.txt')
    print('Task1 on test:', main_function(input_test, ('+', '*')))
    print('Task1 on test:', main_function(input_real, ('+', '*')))
    print('Task1 on test:', main_function(input_test, ('+', '*', '||')))
    print('Task1 on test:', main_function(input_real, ('+', '*', '||')))
