'''Advent of Code. Day 2'''

def is_safe(line):
    '''
    >>> is_safe([7, 6, 4, 2, 1])
    True
    >>> is_safe([1, 2, 7, 8, 9])
    False
    '''
    differences = []
    n = len(line) - 1
    for i, el in enumerate(line[1:]):
        differences.append(line[i] - el)
    return sum(-3 <= i <= -1 for i in differences) == n or sum(1 <= i <= 3 for i in differences) == n


def read_file(pathname: str) -> list:
    '''Read a file
    '''
    with open(pathname, 'r', encoding='utf-8') as file:
        n_safe1, n_safe2 = 0, 0
        for line in file:
            line = list(map(int, line.split()))
            if is_safe(line):
                n_safe1 += 1
                n_safe2 += 1
            else:
                n_safe2 += any(is_safe(line[:j] + line[j+1:]) for j in range(len(line)))
    return n_safe1, n_safe2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task on test:', input_test)
    print('Task on input:', input_real)
