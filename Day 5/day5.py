'''Day 5'''


def read_file(pathname: str) -> tuple[dict[str, set[str]], list[list[str]]]:
    """
    Reads a file and parses its content into a dictionary and a list of lists.

    The file is expected to contain lines with either '|' separated key-value
    pairs or comma-separated values.

    Lines with '|' are added to a dictionary where the key is mapped to
    a set of values.
    Lines with commas are split into lists and added to a list of lists.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        tuple[dict[str, set[str]], list[list[str]]]: A tuple containing
        a dictionary of key-value pairs and a list of lists of strings.
    """
    dct = {}
    data = []
    with open(pathname, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if '|' in line:
                key, value = line.split('|')
                dct.setdefault(key, set()).add(value)
            elif line:
                data.append(line.split(','))
    return dct, data


def main_function(dct: dict[str, set[str]], data: list[list[str]]) -> tuple:
    """
    Processes the data to separate it into correct and incorrect lists
    based on the dictionary.

    Each line in the data is checked against the dictionary. If a line
    contains an element that is a key in the dictionary and the subsequent
    elements are not a subset of the dictionary values for that key, or if
    there is an intersection with previous elements, the line is considered
    incorrect.

    Args:
        dct dict[str, set[str]]: A dictionary mapping keys to sets of values.
        data list[list[str]]: A list of lists of strings to be processed.

    Returns:
        tuple[list[list[str]], list[list[str]]]: A tuple containing two list
        of lists: the first with correct lines and the second with incorrect
        lines.
    """
    result_correct, result_incorrect = [], []
    for line in data:
        for i, el in enumerate(line):
            if (el in dct) and (not (set(line[i+1:]) <= dct[el])
                                or dct[el] & set(line[:i])):
                result_incorrect.append(line)
                break
        else:
            result_correct.append(line)
    return result_correct, result_incorrect


def find_middle(lines: list[list[str]]) -> int:
    """
    Finds the sum of the middle elements of each line in the list.

    Args:
        lines (list[list[str]]): A list of lists of strings, where
        each string is a number.

    Returns:
        int: The sum of the middle elements of each line.
    """
    return sum(int(line[len(line)//2]) for line in lines)


def fix_incorrect(lines: list[list[str]], dct: dict[str, set[str]]) -> list:
    """
    Attempts to fix incorrect lines by sorting elements
    based on the dictionary.

    For each line, elements are sorted such that each element is placed
    before any elements that it maps to in the dictionary.

    Args:
        lines (list[list[str]]): A list of lists of strings to be fixed.
        dct (dict[str, set[str]]): A dictionary mapping keys to sets of values.

    Returns:
        list[list[str]]: A list of lists with the lines sorted according to
        the dictionary.
    """
    result = []
    for line in lines:
        n = len(line)
        if n <= 1:
            return []
        for i in range(1, n):
            key = line[i]
            j = i - 1
            while j >= 0 and key in dct and line[j] in dct[key]:
                line[j+1] = line[j]
                j -= 1
            line[j+1] = key
        result.append(line)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 5/test.txt')
    input_real = read_file('Day 5/input.txt')
    correct_test, incorrect_test = main_function(*input_test)
    correct_real, incorrect_real = main_function(*input_real)
    print('Task1 on test:', find_middle(correct_test))
    print('Task1 on input:', find_middle(correct_real))
    fixed_test = fix_incorrect(incorrect_test, input_test[0])
    fixed_real = fix_incorrect(incorrect_real, input_real[0])
    print('Task2 on test:', find_middle(fixed_test))
    print('Task2 on input:', find_middle(fixed_real))
