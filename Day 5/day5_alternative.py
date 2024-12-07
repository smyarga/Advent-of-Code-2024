"""Day 5"""

from functools import cmp_to_key


def read_file(pathname: str) -> tuple:
    """
    Opens a file and extracts sorting rules and data lines.

    The file should contain two sections separated by a blank line.
    The first section includes sorting rules, and the second section
    contains data lines.

    Args:
        pathname (str): The file path to be opened and read.

    Returns:
        tuple: A tuple containing a comparison function derived from
        the sorting rules and a list of data lines.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        rules, lines = file.read().split('\n\n')
        cmp = cmp_to_key(lambda x, y: -(x+'|'+y in rules))
    return cmp, lines


def main_function(cmp, lines) -> tuple[int, int]:
    """
    Evaluates and categorizes lines of data into correct and incorrect sums.

    Each line is split into elements and sorted using a provided comparison
    function. If the original line matches the sorted line, the middle element
    is added to the correct sum. Otherwise, the middle element of the sorted
    line is added to the incorrect sum.

    Args:
        cmp: A comparison function used to sort elements within each line.
        lines: A string containing multiple lines of comma-separated values.

    Returns:
        tuple[int, int]: A tuple containing two integers: the sum of middle
        elements from correctly sorted lines and the sum of middle elements
        from incorrectly sorted lines.
    """
    result_correct, result_incorrect = 0, 0
    for line in lines.split():
        line = line.split(',')
        sorted_line = sorted(line, key=cmp)
        if line == sorted_line:
            result_correct += int(line[len(line)//2])
        else:
            result_incorrect += int(sorted_line[len(line)//2])
    return result_correct, result_incorrect


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 5/test.txt')
    input_real = read_file('Day 5/input.txt')
    print('Task1 on test:', main_function(*input_test))
    print('Task1 on input:', main_function(*input_real))
    input_test1 = read_file('Day 5/test1.txt')
    print('Task1 on input:', main_function(*input_test1))
