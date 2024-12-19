from functools import lru_cache
def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        possible = sorted(file.readline().strip().split(', '), key=len, reverse=True)
        patterns = [line.strip() for line in file if line.strip()]
    return tuple(possible), patterns

def is_possible(pattern, possible):
    '''
    >>> is_possible('brwrr', ['bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'])
    True
    >>> is_possible('bggr', ['bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'])
    True
    >>> is_possible('gbbr', ['bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'])
    True
    >>> is_possible('ubwu', ['bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'])
    False
    >>> is_possible('bwurrg', ['bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'])
    True
    >>> is_possible('brgr', ['bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'])
    True
    >>> is_possible('bbrgwb', ['bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'])
    False
    '''
    if pattern in possible:
        return True
    pos_start = []
    for start in possible:
        if pattern.startswith(start):
            pos_start.append(pattern[len(start):])
    return any(is_possible(pat, possible) for pat in pos_start)

@lru_cache
def count_possible(pattern, possible):
    '''
    >>> count_possible('brwrr', ('bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'))
    2
    >>> count_possible('bggr', ('bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'))
    1
    >>> count_possible('gbbr', ('bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'))
    4
    >>> count_possible('ubwu', ('bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'))
    0
    >>> count_possible('bwurrg', ('bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'))
    1
    >>> count_possible('brgr', ('bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'))
    2
    >>> count_possible('rrbgbr', ('bwu', 'wr', 'rb', 'gb', 'br', 'r', 'b', 'g'))
    6
    '''
    if pattern == '':
        return 1
    pos_start = set()
    for start in possible:
        if pattern.startswith(start):
            pos_start.add(pattern[len(start):])
    if pos_start:
        return sum(count_possible(pat, tuple(possible)) for pat in pos_start)
    return 0


def main(possible, patterns):
    return sum(is_possible(pat, possible) for pat in patterns)

def main2(possible, patterns):
    return sum(count_possible(pat, possible) for pat in patterns)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 19/test.txt')
    input_real = read_file('Day 19/input.txt')
    print('Task1 on test1:', main(*input_test))
    print('Task1 on input:', main(*input_real))
    print('Task1 on test1:', main2(*input_test))
    print('Task1 on input:', main2(*input_real))