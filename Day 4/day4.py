'''Day 4'''


import itertools


def read_file(pathname: str) -> list[str]:
    """
    Reads a file and returns its content as a list of strings.

    Each line in the file is read and added to a list as a separate string.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        list[str]: A list of strings, each representing a line from the file.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def main_function(rows: list[str]) -> int:
    """
    Counts occurrences of the sequence 'MAS' in specific directions.

    The function checks for the sequence 'MAS' in all possible directions
    (horizontal, vertical, and diagonal) within the given list of strings.

    Args:
        rows (list[str]): A list of strings, each representing
        a row of characters.

    Returns:
        int: The total number of times the sequence 'MAS' appears.
    """
    n = 0
    dirs = list(itertools.product({0, -1, 1}, repeat=2))
    for y, row in enumerate(rows):
        for x, el in enumerate(row):
            for dy, dx in dirs:
                if (el == 'X' and 0 <= y + 3*dy < len(rows)
                        and 0 <= x + 3*dx < len(row)):
                    n += (rows[y + dy][x + dx] + rows[y + 2*dy][x + 2*dx]
                          + rows[y + 3*dy][x + 3*dx] == 'MAS')
    return n


def main_function2(rows: list[str]) -> int:
    """
    Counts occurrences of the sequences 'SAM' and 'MAS' in diagonal directions.

    The function checks for the sequences 'SAM' and 'MAS' in both diagonal
    directions within the given list of strings.

    Args:
        rows (list[str]): A list of strings, each representing a row
        of characters.

    Returns:
        int: The total number of times the sequences 'SAM' and 'MAS' appear
        in the specified diagonal directions.
    """
    n = 0
    for y, row in enumerate(rows):
        for x, el in enumerate(row):
            if 0 <= y + 2 < len(rows) and 0 <= x + 2 < len(row):
                if (el + rows[y + 1][x + 1] + rows[y + 2][x + 2]
                        in ['MAS', 'SAM']):
                    n += (rows[y + 2][x] + 'A' + row[x + 2]) in ['MAS', 'SAM']
    return n


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 4/test.txt')
    input_real = read_file('Day 4/input.txt')
    print('Task on test:', main_function(input_test))
    print('Task on input:', main_function(input_real))
    print('Task on test:', main_function2(input_test))
    print('Task on input:', main_function2(input_real))
