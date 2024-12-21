from functools import wraps
import time
from itertools import combinations
from collections import deque

def timeit(func: callable) -> callable:
    """
    A decorator that measures the execution time of a function.

    Args:
        func (callable): The function to be measured.

    Returns:
        callable: The wrapped function with added timing functionality.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function '{func.__name__}': {(end - start):.6f} seconds")
        return result
    return wrapper

def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        board = {}
        for i, line in enumerate(file):
            for j, el in enumerate(line.strip()):
                board[(i, j)] = el
                if el == 'S':
                    start = (i, j)
                elif el == 'E':
                    end = (i, j)
        return board, start, end


def move(board, start, end, offset=None):
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        position, path = queue.popleft()
        if position == end:
            return set(path)
        if offset and len(path) > offset:
            continue
        x, y = position
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in board and board[(nx, ny)] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return set()

@timeit
def main(board, start, end, m, limit):
    best_path = move(board, start, end)
    min_ = len(best_path)-1
    collisions = set()
    cheats = []
    for (x, y), symb in board.items():
        if symb == '#' and {(x-1, y), (x, y-1), (x+1, y), (x, y+1)}&best_path:
            collisions.add((x, y))
    print(len(collisions))
    for i, (px, py) in enumerate(collisions):
        print(i, end=' ', flush=True)
        board1 = board.copy()
        board1[(px, py)] = '.'
        new_path = move(board1, start, end, min_-limit)
        if new_path:
            cheats.append(len(new_path)-1)
    return sorted({min_-n: cheats.count(n) for n in cheats if min_-n >= limit}.items())



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test1 = read_file('Day 20/test.txt')
    input_real = read_file('Day 20/input.txt')
    print('Task on test1:', len(move(*input_test1))-1)
    print('Task on input:', len(move(*input_real))-1)
    print('Task on test1:', main(*input_test1, 2, 1))
    print('Task on test1:', main(*input_real, 2, 100))
    # print('Task on test1:', main(*input_test1, 20, 1))

# @timeit
# def move(bytes, size, steps):
#     start = (0, 0)
#     end = (size-1, size-1)
#     grid = {(i, j): '.' for i in range(size) for j in range(size)}
#     for (bx, by) in bytes[:steps]:
#         grid[(by, bx)] = '#'
#     # grid1 = [[None]*(size) for _ in range(size)]
#     # for key, val in grid.items():
#     #     grid1[key[0]][key[1]] = val
#     # print('\n'.join([''.join(row) for row in grid1]))
#     paths = {start: {start}}
#     routes = []
#     while paths and end not in paths:
#         for end_point, path in paths.copy().items():
#             del paths[end_point]
#             px, py = end_point
#             for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
#                 newx, newy = px+dx, py+dy
#                 if (newx, newy) in grid and grid[(newx, newy)] != '#' and (newx, newy) not in path:
#                     path_new = path | {(newx, newy)}
#                     if ((newx, newy)) not in paths:
#                         paths[(newx, newy)] = path_new
#     routes.append(paths[end])
#     print(routes)
#     return [len(route)-1 for route in routes]


# def find_break(bytes, size):
#     start, end = 1, len(bytes)
#     middle = (end+start)//2
#     while True:
#         first = move(bytes, size, middle)
#         if not first:
#             end = middle
#             middle = (end+start)//2
#         next = move(bytes, size,  middle+1)
#         if not next:
#             return bytes[middle]
#         start = middle
#         middle = (end+start)//2


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
#     input_test = read_file('Day 18/test.txt')
#     input_real = read_file('Day 18/input.txt')
#     print('Task1 on test1:', move(input_test, 7, 12))
#     print('Task1 on input:', move(input_real, 71, 1024))
#     # print('Task2 on test1:', find_break(input_test, 7))
#     # print('Task2 on test1:', find_break(input_real, 71))

