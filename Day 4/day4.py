import itertools

def read_file(pathname: str) -> list[list[str]]:
    """
    >>> read_file('test.txt')
    ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def main_function(rows: list[list[str]]) -> int:
    n = 0
    dirs = list(itertools.product({0, -1, 1}, repeat=2))
    for y, row in enumerate(rows):
        for x, el in enumerate(row):
            for dy, dx in dirs:
                if el == 'X' and 0 <= y + 3*dy < len(rows) and 0 <= x + 3*dx < len(rows):
                    n += (rows[y + dy][x + dx]+rows[y + 2*dy][x + 2*dx]+rows[y + 3*dy][x + 3*dx] == 'MAS')
    return n


def main_function2(rows: list[list[str]]) -> int:
    n = 0
    for y, row in enumerate(rows):
        for x, el in enumerate(row):
            if 0 <= y + 2 < len(rows) and 0 <= x + 2 < len(row):
                if (el + rows[y + 1][x + 1] + rows[y + 2][x + 2]) in ['MAS', 'SAM']:
                    n += (rows[y+2][x] + 'A' + row[x+2]) in ['MAS', 'SAM']
    return n


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('test.txt')
    input_real = read_file('input.txt')
    print('Task on test:', main_function(input_test))
    print('Task on input:', main_function(input_real))
    print('Task on test:', main_function2(input_test))
    print('Task on input:', main_function2(input_real))