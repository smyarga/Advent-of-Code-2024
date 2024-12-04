
def read_file(pathname: str) -> list[list[str]]:
    """
    >>> read_file('test.txt')
    []
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def main_function(rows: list[list[str]]) -> int:
    return rows

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task on test:', main_function(input_test))
    print('Task on input:', main_function(input_real))