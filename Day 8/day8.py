'''Day 8'''
from itertools import permutations, count


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
        return {(i, j): el for i, line in enumerate(file)
                for j, el in enumerate(line.strip())}


def trace_path(grid: dict[tuple[int, int], str],
               start: tuple[int],
               slope: tuple[int],
               can_repeat: bool) -> set:
    """Trace along a line defined by start + n*slope,
    stopping if out of grid or if repeat=False."""
    antinodes = set()
    x, y = start
    dx, dy = slope
    for i in count(1):
        coord = (x + dx*i, y + dy*i)
        if coord in grid:
            antinodes.add(coord)
        else:
            break
        if not can_repeat:
            break
    return antinodes


def main_function(grid: list[str], repeat=False) -> int:
    """
    Determines the number of obstacles encountered when simulating path
    traversal with different starting conditions.

    Args:
        rows (List[str]): A list of strings representing the grid
        with directions.

    Returns:
        int: The number of unique obstacles encountered.
    """
    antennas = set(grid.values()) - {'.'}
    antinodes = set()
    for symbol in antennas:
        coord_symb = {key for key, symb in grid.items() if symb == symbol}
        for (x1, y1), (x2, y2) in permutations(coord_symb, 2):
            slope_x, slope_y = (x2-x1, y2-y1)
            antinodes |= trace_path(grid,
                                    (x2, y2),
                                    (slope_x, slope_y),
                                    repeat)
            antinodes |= trace_path(grid,
                                    (x1, y1),
                                    (-slope_x, -slope_y),
                                    repeat)
            if repeat:
                antinodes |= trace_path(grid,
                                        (x2, y2),
                                        (-slope_x, -slope_y),
                                        repeat)

    return len(antinodes)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 8/test.txt')
    input_real = read_file('Day 8/input.txt')
    print('Task1 on test:', main_function(input_test))
    print('Task1 on input:', main_function(input_real))
    input_test2 = read_file('Day 8/test2.txt')
    print('Task2 on test2:', main_function(input_test2, True))
    print('Task2 on test:', main_function(input_test, True))
    print('Task2 on input:', main_function(input_real, True))
