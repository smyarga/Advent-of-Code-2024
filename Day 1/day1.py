'''Advent of Code. Day 1'''


def read_file(pathname: str) -> tuple[list]:
    '''Read a file and return a tuple of two lists.

    The file should contain pairs of integers separated by spaces,
    one pair per line.
    Each integer pair is split into two lists: left and right.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        tuple[list]: A tuple containing two lists of integers.
    '''
    with open(pathname, 'r', encoding='utf-8') as file:
        left, right = zip(*(map(int, line.strip().split()) for line in file))
        return left, right


def find_diff_id(left: list, right: list) -> int:
    '''Find the total difference between elements of two lists.

    The function pairs up the smallest number in the left list with
    the smallest number in the right list, the second-smallest with
    the second-smallest, and so on. It then calculates the absolute
    difference for each pair and returns the sum of these differences.

    Args:
        left (list): The first list of integers.
        right (list): The second list of integers.

    Returns:
        int: The total difference between the paired elements of the two lists.
    '''
    return sum(abs(l_val - r_val) for l_val, r_val in zip(sorted(left), sorted(right)))


def find_similarity(left: list, right: list) -> int:
    '''Find the similarity score between two lists.

    The function calculates the similarity score by multiplying each number
    in the left list by the number of times it appears in the right list,
    and then summing these products.

    Args:
        left (list): The first list of integers.
        right (list): The second list of integers.

    Returns:
        int: The similarity score between the two lists.
    '''
    return sum(numb*right.count(numb) for numb in left)  # sum(x for x in right if x in set(left))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task 1.1 Difference on test:', find_diff_id(*input_test))
    print('Task 1.1 Difference on input:', find_diff_id(*input_real))
    print('Task 1.2 Similarity on test:', find_similarity(*input_test))
    print('Task 1.2 Similarity on input:', find_similarity(*input_real))

    # with open('input.txt', 'r', encoding='utf-8') as file:
    #     left, right = zip(*(map(int, line.strip().split()) for line in file))
    #     print('Part 1:', sum(abs(r_val - l_val) for l_val, r_val in zip(sorted(left), sorted(right))))
    #     print('Part 2:', sum(numb*right.count(numb) for numb in left))
    #     print('Part 2:', sum(x for x in right if x in set(left)))
