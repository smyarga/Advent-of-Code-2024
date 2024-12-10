'''Day 9'''
from itertools import count
import sys
sys.setrecursionlimit(300000)

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
    '0..111....22222'
    >>> decode('2333133121414131402')
    '00...111...2...333.44.5555.6666.777.888899'
    '''
    id = 0
    out = ''
    for i, el in enumerate(number):
        if i%2 == 0:
            out += str(id)*int(el)
            id += 1
        else:
            out += '.'*int(el)
    return out

def move(decoded_number: str, depth=0) -> str:
    '''
    >>> move('0..111....22222')
    '022111222'
    >>> move('00...111...2...333.44.5555.6666.777.888899')
    '0099811188827773336446555566'
    '''
    # n = len(decoded_number)
    stripped = decoded_number.strip('.')
    if '.' not in stripped:
        return stripped
    i = stripped.index('.')
    return move(stripped[:i]+stripped[-1]+stripped[i+1:-1], depth+1)

    # print(n)
    # for i, el in enumerate(decoded_number):
    #     # print(i, end=' ', flush=True)
    #     if set(decoded_number[i+1:]) <= {'.'}:
    #         break
    #     if el == '.':
    #         decoded_number = decoded_number.strip('.')
    #         decoded_number = decoded_number[:i] +  decoded_number[-1]+ decoded_number[i+1:-1]
    # return decoded_number+'.'*(n-len(decoded_number))

def find_checksum(number):
    '''
    >>> find_checksum('0099811188827773336446555566..............')
    1928
    '''
    number = number.strip('.')
    return sum(i*int(el) for i, el in enumerate(number))


def main(grid):
    '''main function'''
    return grid


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 9/test.txt')
    input_real = read_file('Day 9/input.txt')
    # print(input_real)
    print('Task1 on test:', main(input_test))
    # print('Task1 on input:', main(input_real))
    print(find_checksum(move(decode(input_test))))
    # decoded = decode(input_real)
    # print(decoded)
    # moved = move(decoded)
    # print(moved)
    # print(find_checksum(moved))
