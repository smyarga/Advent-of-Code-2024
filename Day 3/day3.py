import re

def mul(a, b):
    '''
    >>> mul(2,4)
    8
    '''
    return a*b


def read_file(pathname: str) -> list:
    '''
    >>> read_file('test.txt')
    [['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']]
    '''
    with open(pathname, 'r', encoding='utf-8') as file:
        return [re.findall(r"mul\(\d*?,\d*?\)", line) for line in file]


def read_file2(pathname: str) -> list:
    '''
    >>> read_file2('test1.txt')
    [['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']]
    '''
    with open(pathname, 'r', encoding='utf-8') as file:
        return [re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line) for line in file]


def main_function(rows: list) -> int:
    return sum(sum(map(eval, row)) for row in rows)


def main_function2(rows: list) -> int:
    '''
    >>> main_function2([['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']])
    48
    '''
    result = 0
    flag = True
    for row in rows:
        for el in row:
            if el == "don't()":
                flag = False
            elif el == 'do()':
                flag = True
            elif flag:
                result += eval(el)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task on test:', main_function(input_test))
    print('Task on input:', main_function(input_real))
    print('Task2 on test:', main_function2(read_file2('test1.txt')))
    print('Task2 on input:',main_function2(read_file2('input.txt')))
