'''Day 6'''
from itertools import cycle


def read_file(pathname: str) -> list[str]:
    """
    Reads a file and returns its content as a list of strings.

    Each line in the file is read and added to a list as a separate string.

    Args:
        pathname (str): The path to the file to be read.

    Returns:
        List[str]: A list of strings, each representing a line from the file.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def main_function(rows: list[str]) -> tuple[tuple[int, int], set[tuple[int, int]], int]:
    """
    Simulates a path traversal based on given directions and returns
    the starting position, the set of visited positions, and the count
    of unique positions visited.

    Args:
        rows (List[str]): A list of strings representing the grid with
        directions.

    Returns:
        Tuple[Tuple[int, int], Set[Tuple[int, int]], int]: A tuple containing
        the starting position, the set of visited positions, and the count of
        unique positions visited.
    """
    directions = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    turn = cycle('>v<^')
    cur_dir = '^'
    for i, row in enumerate(rows):
        if cur_dir in row:
            st_x, st_y = i, row.index(cur_dir)
    cur_x, cur_y = st_x, st_y
    path = set()

    while True:
        path.add((cur_x, cur_y))
        dx, dy = directions[cur_dir]
        next_x, next_y = cur_x + dx, cur_y + dy
        if 0 <= next_x < len(rows) and 0 <= next_y < len(rows[0]):
            if rows[next_x][next_y] == '#':
                cur_dir = next(turn)
            else:
                cur_x, cur_y = next_x, next_y
        else:
            break
    return (st_x, st_y), path, len(set(path))


def main_function2(rows: list[str]) -> int:
    """
    Determines the number of obstacles encountered when simulating path traversal
    with different starting conditions.

    Args:
        rows (List[str]): A list of strings representing the grid with directions.

    Returns:
        int: The number of unique obstacles encountered.
    """
    (st_x, st_y), path_all = main_function(rows)[:2]
    directions = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
    obstacles = []
    for el in set(path_all) - set((st_x, st_y)):
        turn = cycle('>v<^')
        rows_new = [list(row) for row in rows]
        rows_new[el[0]][el[1]] = '#'
        cur_x, cur_y = st_x, st_y
        cur_dir = '^'
        path = set()
        while True:
            path.add((cur_x, cur_y, cur_dir))
            dx, dy = directions[cur_dir]
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < len(rows_new) and 0 <= next_y < len(rows_new[0]):
                if rows_new[next_x][next_y] == '#':
                    cur_dir = next(turn)
                elif (next_x, next_y, cur_dir) in path:
                    obstacles.append((el[0], el[1]))
                    break
                else:
                    cur_x, cur_y = next_x, next_y
            else:
                break
    return len(set(obstacles))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 6/test.txt')
    input_real = read_file('Day 6/input.txt')
    print('Task1 on test:', main_function(input_test)[2])
    print('Task1 on input:', main_function(input_real)[2])
    print('Task2 on test:', main_function2(input_test))
    # (6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)
    print('Task2 on test:', main_function2(input_real))