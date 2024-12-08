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
                for j, el in enumerate(line.strip())}


def main(grid):
    return grid


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 9/test.txt')
    input_real = read_file('Day 9/input.txt')
    print('Task1 on test:', main(input_test))
    print('Task1 on input:', main(input_real))