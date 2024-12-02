def read_file(pathname: str) -> list:
    '''
    >>> read_file('test.txt')
    [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], \
[8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
    '''
    with open(pathname, 'r', encoding='utf-8') as file:
        return [list(map(int, line.split())) for line in file]


def main_function(rows: list) -> int:
    return rows


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task on test:', main_function(input_test))
    print('Task on input:', main_function(input_real))
