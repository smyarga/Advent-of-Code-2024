'''Advent of Code. Day 1'''


def read_file(pathname: str) -> list:
    '''read'''
    with open(pathname, 'r', encoding='utf-8') as file:
        left, right = zip(*(map(int, line.strip().split()) for line in file))
        return sorted(left), sorted(right)


def find_diff_id(left: list, right: list) -> int:
    '''find difference between elements of two lists'''
    return sum(abs(right[i]-val) for i, val in enumerate(left))


def find_similarity(left: list, right: list) -> int:
    '''find similarity score'''
    return sum(numb*right.count(numb) for numb in left)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task 1.1 Difference on test:', find_diff_id(*input_test))
    print('Task 1.1 Difference on input:', find_diff_id(*input_real))
    print('Task 1.2 Similarity on test:', find_similarity(*input_test))
    print('Task 1.2 Similarity on input:', find_similarity(*input_real))
