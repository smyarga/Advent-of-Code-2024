from itertools import product

def read_file(pathname: str) -> list[str]:
    """
    Reads a file and returns its content as a list of strings.

    Each line in the file is read and added to a list as a separate string.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        list[str]: A list of strings, each representing a line from the file.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return [(int(key), list(map(int, values.split())))
                for key, values in (line.strip().split(':') for line in file)]


def main_function(dct: list, symbols: set) -> int:
    output = 0
    for key, values in dct:
        signs = product(symbols, repeat=len(values)-1)
        for comb in signs:
            result = values[0]
            for i, el in enumerate(values[1:]):
                if comb[i] == '+':
                    result += el
                elif comb[i] == '*':
                    result *= el
                elif comb[i] == '||':
                    result = int(str(result) + str(el))
            if result == key:
                output += key
                break
    return output



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 7/test.txt')
    input_real = read_file('Day 7/input.txt')
    # print(input_test)
    print('Task1 on test:', main_function(input_test, {'+', '*'}))
    print('Task1 on test:', main_function(input_real, {'+', '*'}))
    print('Task1 on test:', main_function(input_test, {'+', '*', '||'}))
    print('Task1 on test:', main_function(input_real, {'+', '*', '||'}))
    # print('Task1 on test:', main_function(input_real, {'+', '*'}))
    # print('Task1 on input:', main_function(input_real)[2])
    # print('Task2 on test:', main_function2(input_test))
    # # (6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)
    # print('Task2 on test:', main_function2(input_real))