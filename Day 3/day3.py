import re
# from operator import mul
import math


def read_file(pathname: str) -> list[list[str]]:
    """
    Reads a file and extracts all occurrences of 'mul' function calls.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        list[list[str]]: A list of lists containing strings that
                            match the pattern 'mul(a,b)'.

    Example:
    >>> read_file('test.txt')
    [[('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]]
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return [re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line) for line in file]


def read_file2(pathname: str) -> list[list[str]]:
    """
    Reads a file and extracts all occurrences of
    'mul', 'don't', and 'do' function calls.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        list[list[str]]: A list of lists containing strings that
                match the patterns 'mul(a,b)', "don't()", or 'do()'.

    Example:
    >>> read_file2('test1.txt')
    [[('2', '4', '', ''), ('', '', "don't()", ''), ('5', '5', '', ''), ('11', '8', '', ''), ('', '', '', 'do()'), ('8', '5', '', '')]]
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return [re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))", line) for line in file]


def main_function(rows: list[list[str]]) -> int:
    """
    Evaluates and sums up all 'mul' function calls in
    the provided list of lists.

    Args:
        rows (list[list[str]]): A list of lists containing
        strings of 'mul' function calls.

    Returns:
        int: The sum of all evaluated 'mul' function calls.

    Example:
    >>> main_function([[('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]])
    161
    """
    return sum(sum(map(lambda x: int(x[0])*int(x[1]), row)) for row in rows)


def main_function2(rows: list[list[str]]) -> int:
    """
    Evaluates and sums up 'mul' function calls in the provided list of lists, 
    respecting 'do' and "don't" commands to control evaluation.

    Args:
        rows (list[list[str]]): A list of lists containing strings
        of 'mul', 'do', and "don't" function calls.

    Returns:
        int: The sum of all evaluated 'mul' function calls, controlled
        by 'do' and "don't" commands.

    Example:
    >>> main_function2([[('2', '4', '', ''), ('', '', "don't()", ''), ('5', '5', '', ''), ('11', '8', '', ''), ('', '', '', 'do()'), ('8', '5', '', '')]])
    48
    """
    result = 0
    flag = True
    for row in rows:
        for a, b, dont, do in row:
            if do:
                flag = True
            elif dont:
                flag = False
            elif flag:
                result += int(a)*int(b)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task on test:', main_function(input_test))
    print('Task on input:', main_function(input_real))
    print('Task2 on test:', main_function2(read_file2('test1.txt')))
    print('Task2 on input:', main_function2(read_file2('input.txt')))
