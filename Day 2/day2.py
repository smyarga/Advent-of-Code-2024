'''Advent of Code. Day 2'''


def read_file(pathname: str) -> list:
    '''Read a file
    '''
    with open(pathname, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    # print('Task 1.1 on test:', find_diff_id(*input_test))
    # print('Task 1.1 on input:', find_diff_id(*input_real))
    # print('Task 1.2 on test:', find_similarity(*input_test))
    # print('Task 1.2 on input:', find_similarity(*input_real))