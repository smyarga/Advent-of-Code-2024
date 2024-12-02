'''Advent of Code. Day 2'''


def is_safe(line: list[int]) -> bool:
    '''
    Determine if a line is safe based on the differences
    between consecutive elements.
    
    A line is considered safe if the differences between
    consecutive elements are all within
    the range of -3 to -1 or 1 to 3.

    Parameters:
    line (list of int): A list of integers representing
    the line to be checked.

    Returns:
    bool: True if the line is safe, False otherwise.

    Examples:
    >>> is_safe([7, 6, 4, 2, 1])
    True
    >>> is_safe([1, 2, 7, 8, 9])
    False
    '''
    differences = {line[i] - el for i, el in enumerate(line[1:])}
    return differences <= {-3, -2, -1} or differences <= {1, 2, 3} 


def read_file(pathname: str) -> list:
    '''Read a file and convert its contents to a list of lists of integers.

    Parameters:
    pathname (str): The path to the file to be read.

    Returns:
    list of list of int: A list where each element is a list of integers
    representing a line from the file.

    Examples:
    >>> read_file('test.txt')
    [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], \
[8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
    '''
    with open(pathname, 'r', encoding='utf-8') as file:
        return [list(map(int, line.split())) for line in file]


def number_safe(rows: list[list[int]]) -> int:
    '''
    Count the number of safe lines and the number of lines that
    can be made safe by removing one element.

    Parameters:
    rows (list of list of int): A list where each element is a list of integers
    representing a line to be checked.

    Returns:
    tuple: A tuple containing two integers:
        - The number of safe lines.
        - The total number of lines that are either safe or can be made safe
          by removing one element.

    Examples:
    >>> number_safe([[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1]])
    (1, 1)
    >>> number_safe([[1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    (1, 3)
    '''
    n_safe1, n_safe2 = 0, 0
    for line in rows:
        safe1 = is_safe(line)
        n_safe1 += safe1
        if not safe1:
            n_safe2 += any(is_safe(line[:j] + line[j+1:]) for j in range(len(line)))
    return n_safe1, n_safe1 + n_safe2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task on test:', number_safe(input_test))
    print('Task on input:', number_safe(input_real))
