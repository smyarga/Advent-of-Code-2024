'''Day 4'''


def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.

    Each character in the file is mapped to a tuple representing its
    position in the file, with the first element of the tuple being
    the line index and the second being the character index.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        dict[tuple[int, int], str]: A dictionary where keys are tuples
        representing the position of each character, and values are the
        characters themselves.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return {(i, j): el for i, line in enumerate(file)
                for j, el in enumerate(line)}


def main_function(dct: dict[tuple[int, int], str]) -> int:
    """
    Counts occurrences of the sequence 'XMAS' in all possible directions.

    The function checks for the sequence 'XMAS' in all possible directions
    (horizontal, vertical, and diagonal) within the given dictionary.

    Args:
        dct (dict[tuple[int, int], str]): A dictionary with keys as tuples
        representing positions and values as characters.

    Returns:
        int: The total number of times the sequence 'XMAS' appears.
    """
    dirs = {0, -1, 1}
    return sum(''.join(dct.get((i + di * n, j + dj * n), '')
                       for n in range(4)) == 'XMAS'
               for i, j in dct for di in dirs for dj in dirs)


def main_function2(dct: dict[tuple[int, int], str]) -> int:
    """
    Counts occurrences of the sequences 'SAM' and 'MAS' in diagonal directions.

    The function checks for the sequences 'SAM' and 'MAS' in both diagonal
    directions within the given dictionary.

    Args:
        dct (dict[tuple[int, int], str]): A dictionary with keys as tuples
        representing positions and values as characters.

    Returns:
        int: The total number of times the sequences 'SAM' and 'MAS' appear
        in the specified diagonal directions.
    """
    xmas = {'SAM', 'MAS'}
    return sum(''.join(dct.get((i + d, j + d), '')
                       for d in (-1, 0, 1)) in xmas
               and ''.join(dct.get((i + d, j - d), '')
                           for d in (-1, 0, 1)) in xmas
               for i, j in dct)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 4/test.txt')
    input_real = read_file('Day 4/input.txt')
    print('Task on test:', main_function(input_test))
    print('Task on input:', main_function(input_real))
    print('Task on test:', main_function2(input_test))
    print('Task on input:', main_function2(input_real))
