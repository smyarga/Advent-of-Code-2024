'''Advent of Code. Day 2'''

def is_safe(line):
    '''
    >>> is_safe([7, 6, 4, 2, 1])
    True
    >>> is_safe([1, 2, 7, 8, 9])
    False
    '''
    differences = {line[i] - el for i, el in enumerate(line[1:])}
    return differences <= {-3, -2, -1} or differences <= {1, 2, 3} 


def read_file(pathname: str) -> list:
    '''Read a file
    '''
    with open(pathname, 'r', encoding='utf-8') as file:
        n_safe1, n_safe2 = 0, 0
        for line in file:
            line = list(map(int, line.split()))
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
    print('Task on test:', input_test)
    print('Task on input:', input_real)
