'''Day 9'''
import sys
sys.setrecursionlimit(30000)

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
        return file.read().strip()


def decode(number: str) -> str:
    '''
    >>> decode('12345')
    [(0, 1), ('.', 2), (1, 3), ('.', 4), (2, 5)]
    >>> decode('2333133121414131402')
    [(0, 2), ('.', 3), (1, 3), ('.', 3), (2, 1), ('.', 3), (3, 3), ('.', 1), (4, 2), ('.', 1), (5, 4), ('.', 1), (6, 4), ('.', 1), (7, 3), ('.', 1), (8, 4), (9, 2)]
    '''
    id = 0
    out = []
    for i, el in enumerate(number):
        if i%2 == 0:
            out.append((id, int(el)))
            id += 1
        else:
            if int(el) != 0:
                out.append(('.', int(el)))
    return out


def joined(lst1, lst2):
    if lst1 == [] or lst2 == []:
        return lst1+lst2
    if lst1[-1][0] == lst2[0][0]:
        return lst1[:-1]+[(lst1[-1][0], lst1[-1][1]+lst2[0][1])]+lst2[1:]
    return lst1+lst2


def move(decoded_number: str, depth=0) -> str:
    '''
    >>> move([(0, 1), ('.', 2), (1, 3), ('.', 4), (2, 5)])
    [(0, 1), (2, 2), (1, 3), (2, 3)]

    >>> move([(0, 2), ('.', 3), (1, 3), ('.', 3), (2, 1), ('.', 3), (3, 3), ('.', 1), (4, 2), ('.', 1), (5, 4), ('.', 1), (6, 4), ('.', 1), (7, 3), ('.', 1), (8, 4), (9, 2)])
    [(0, 2), (9, 2), (8, 1), (1, 3), (8, 3), (2, 1), (7, 3), (3, 3), (6, 1), (4, 2), (6, 1), (5, 4), (6, 2)]
    '''
    if len(decoded_number) == 0:
        return []
    if decoded_number[0][0] != '.':
        for i, (symb, _) in enumerate(decoded_number):
            if symb == '.':
                return joined(decoded_number[:i], move(decoded_number[i:], depth+1))
    _, n = decoded_number[0]
    last, m = decoded_number[-1]
    if last == '.':
        return move(decoded_number[:-1], depth+1)
    if len(decoded_number) == 2:
        return [decoded_number[1]]
    if n < m:
        decoded_number[0] = (last, n)
        decoded_number[-1] = (last, m-n)
    elif n == m:
        decoded_number[0] = (last, n)
        decoded_number.pop()
    else:
        decoded_number.insert(0, (last, m))
        decoded_number[1] = ('.', n-m)
        decoded_number.pop()
    return move(decoded_number, depth+1)



def move2(decoded_number: str) -> str:
    '''
    >>> move2([(0, 2), ('.', 3), (1, 3), ('.', 3), (2, 1), ('.', 3), (3, 3), ('.', 1), (4, 2), ('.', 1), (5, 4), ('.', 1), (6, 4), ('.', 1), (7, 3), ('.', 1), (8, 4), (9, 2)])
    [(0, 2), (9, 2), (2, 1), (1, 3), (7, 3), ('.', 1), (4, 2), ('.', 1), (3, 3), ('.', 4), (5, 4), ('.', 1), (6, 4), ('.', 5), (8, 4), ('.', 2)]
    '''
    if len(decoded_number) == 1:
        return decoded_number
    symb, n = decoded_number[-1]
    if symb == '.':
        return joined(move2(decoded_number[:-1]), [decoded_number[-1]])
    if decoded_number[0][0] != '.':
        return joined([decoded_number[0]], move2(decoded_number[1:]))
    for k, (s, m) in enumerate(decoded_number[:-1]):
        if s == '.' and m >= n:
            if m > n:
                decoded_number.insert(k, (symb, n))
                decoded_number[k+1] = ('.', m-n)
            elif m == n:
                decoded_number[k] = (symb, m)
            decoded_number.pop()
            if decoded_number[-1][0] == '.':
                decoded_number[-1] = ('.', decoded_number[-1][1]+n)
            else:
                decoded_number += [('.', n)]
            break
    return joined(move2(decoded_number[:-1]), [decoded_number[-1]])


def find_checksum(number):
    '''
    >>> find_checksum([(0, 1), ('.', 2), (1, 3), ('.', 4), (2, 5)])
    132
    >>> find_checksum([(0, 2), (9, 2), (8, 1), (1, 3), (8, 3), (2, 1), (7, 1), (7, 2), (3, 3), (6, 1), (4, 2), (6, 1), (5, 4), (6, 1), (6, 1)])
    1928
    >>> find_checksum([(0, 2), (9, 2), (2, 1), (1, 3), (7, 3), ('.', 1), (4, 2), ('.', 1), (3, 3), ('.', 4), (5, 4), ('.', 1), (6, 4), ('.', 5), (8, 4), ('.', 2)])
    2858
    '''
    out = 0
    k = 0
    for id, n in number:
        if id == '.':
            k += n
            continue
        for i in range(n):
            out += id*(i+k)
        k += n
    return out


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 9/test.txt')
    input_real = read_file('Day 9/input.txt')
    print('Task1 on test:', find_checksum(move(decode(input_test))))
    print('Task1 on input:', find_checksum(move(decode(input_real))))
    print('Task2 on test:', find_checksum(move2(decode(input_test))))
    print('Task2 on input:', find_checksum(move2(decode(input_real))))
