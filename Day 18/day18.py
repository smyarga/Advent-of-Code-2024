from functools import wraps
import time

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
        return [tuple(map(int, line.strip().split(','))) for line in file]

@timeit
def move(bytes, size, steps):
    start = (0, 0)
    end = (size-1, size-1)
    grid = {(i, j): '.' for i in range(size) for j in range(size)}
    for (bx, by) in bytes[:steps]:
        grid[(by, bx)] = '#'
    # grid1 = [[None]*(size) for _ in range(size)]
    # for key, val in grid.items():
    #     grid1[key[0]][key[1]] = val
    # print('\n'.join([''.join(row) for row in grid1]))
    paths = {start: {start}}
    routes = []
    while paths and end not in paths:
        for end_point, path in paths.copy().items():
            del paths[end_point]
            px, py = end_point
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newx, newy = px+dx, py+dy
                if (newx, newy) in grid and grid[(newx, newy)] != '#' and (newx, newy) not in path:
                    path_new = path | {(newx, newy)}
                    if ((newx, newy)) not in paths:
                        paths[(newx, newy)] = path_new
    routes.append(paths[end])
    print(routes)
    return [len(route)-1 for route in routes]

# @timeit
# def move(bytes, size, steps):
#     start = (0, 0)
#     end = (size-1, size-1)
#     grid = {(i, j): '.' for i in range(size) for j in range(size)}
#     for (bx, by) in bytes[:steps]:
#         grid[(by, bx)] = '#'
#     grid1 = [[None]*(size) for _ in range(size)]
#     right_path = {(12, 4), (4, 0), (34, 1), (70, 55), (64, 14), (70, 64), (8, 0), (19, 0), (30, 0), (56, 28), (60, 10), (38, 7), (70, 39), (18, 10), (70, 48), (34, 3), (64, 16), (70, 66), (22, 10), (19, 2), (30, 2), (41, 8), (60, 21), (60, 30), (26, 7), (49, 9), (18, 3), (70, 50), (53, 9), (70, 59), (22, 3), (64, 18), (70, 68), (22, 12), (66, 46), (30, 4), (0, 0), (63, 38), (15, 0), (26, 0), (60, 32), (67, 38), (18, 5), (70, 43), (70, 52), (14, 1), (70, 70), (14, 10), (66, 48), (19, 6), (56, 25), (11, 2), (26, 2), (60, 34), (70, 45), (70, 54), (34, 0), (70, 63), (45, 9), (56, 9), (14, 3), (66, 50), (11, 4), (15, 4), (25, 6), (7, 0), (18, 0), (70, 38), (18, 9), (70, 56), (22, 0), (34, 2), (64, 15), (37, 7), (60, 20), (10, 1), (59, 22), (26, 6), (25, 8), (18, 2), (70, 40), (70, 49), (40, 8), (22, 2), (34, 4), (66, 36), (22, 11), (69, 62), (41, 9), (52, 9), (60, 22), (67, 46), (18, 4), (70, 42), (70, 51), (22, 4), (3, 0), (14, 0), (66, 38), (62, 34), (10, 5), (26, 1), (70, 44), (63, 14), (69, 48), (14, 2), (66, 49), (59, 10), (33, 0), (62, 36), (44, 9), (48, 9), (21, 10), (14, 4), (10, 0), (62, 38), (59, 30), (68, 60), (40, 7), (22, 1), (63, 18), (10, 2), (68, 62), (66, 37), (55, 9), (36, 5), (28, 1), (62, 33), (10, 4), (2, 0), (25, 2), (58, 29), (69, 38), (6, 0), (61, 34), (69, 56), (36, 7), (28, 3), (68, 48), (10, 6), (68, 57), (32, 3), (58, 22), (24, 8), (29, 4), (69, 40), (21, 0), (61, 36), (62, 10), (69, 58), (62, 19), (65, 36), (47, 9), (68, 41), (62, 37), (68, 50), (51, 9), (58, 24), (61, 20), (13, 10), (24, 10), (69, 42), (16, 6), (62, 12), (69, 60), (68, 61), (24, 3), (24, 12), (64, 48), (16, 8), (21, 4), (62, 14), (20, 8), (17, 0), (28, 0), (62, 32), (58, 10), (32, 0), (43, 9), (58, 28), (24, 5), (35, 5), (69, 46), (16, 10), (20, 10), (36, 6), (12, 6), (5, 0), (28, 2), (68, 38), (68, 56), (32, 2), (58, 30), (65, 17), (39, 7), (20, 3), (62, 18), (12, 8), (28, 4), (68, 40), (9, 0), (68, 49), (61, 10), (68, 58), (32, 4), (58, 23), (64, 36), (24, 9), (16, 5), (62, 11), (57, 24), (62, 20), (65, 46), (12, 10), (68, 42), (1, 0), (24, 2), (64, 38), (24, 11), (64, 47), (16, 7), (62, 13), (20, 7), (54, 9), (12, 3), (65, 48), (23, 12), (58, 9), (18, 8), (19, 8), (56, 27), (24, 4), (35, 4), (16, 0), (61, 32), (16, 9), (20, 0), (31, 0), (60, 36), (57, 28), (68, 46), (70, 65), (30, 1), (19, 10), (24, 6), (11, 6), (65, 16), (20, 2), (31, 2), (12, 7), (70, 58), (70, 67), (50, 9), (16, 4), (65, 18), (60, 31), (26, 8), (20, 4), (31, 4), (12, 9), (70, 60), (27, 0), (70, 69), (56, 24), (64, 37), (64, 46), (15, 10), (20, 6), (18, 6), (12, 2), (70, 53), (70, 62), (42, 9), (56, 26), (46, 9), (57, 9), (60, 35), (67, 50), (70, 46)}
#     for key, val in grid.items():
#         grid1[key[0]][key[1]] = val
#     print('\n'.join([''.join(row) for row in grid1]))
#     paths = {(start, (0, 1)): [start]}
#     routes = []
#     # flag = False
#     while paths and not routes:
#         for (end_point, cur_dir), path in paths.copy().items():
#             if set(path) <= right_path:
#                 print(end_point, path)
#             del paths[(end_point, cur_dir)]
#             px, py = end_point
#             if (px, py) == end:
#                 routes.append(path)
#                 continue
#             # if (px, py) in [(36, 7)]:
#             #     flag = True
#             while True:
#                 pos_ways = []
#                 for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
#                     newx, newy = px+dx, py+dy
#                     if (newx, newy) in grid and grid[(newx, newy)] != '#' and (newx, newy) not in path:
#                         path_new = path + [(newx, newy)]
#                         pos_ways.append((((newx, newy), (dx, dy)), path_new))
#                 # if flag:
#                 #     print(px, py, [x for x, _ in pos_ways])
#                 if len(pos_ways) != 1:
#                     break
#                 ((px, py), cur_dir), path = pos_ways[0]
            
#             if pos_ways:
#                 # print((newx, newy), pos_ways)
#                 for (((newx, newy), (dx, dy)), path_new) in pos_ways:
#                     if ((newx, newy), (dx, dy)) not in paths or len(path_new) < len(paths[((newx, newy), (dx, dy))]):
#                         paths[((newx, newy), (dx, dy))] = path_new
#                     elif len(path_new) == len(paths[((newx, newy), (dx, dy))]):
#                         paths[((newx, newy), (dx, dy))] += path_new 

#             flag = False
#     # for key in routes[0][0]:
#     #     grid1[key[0]][key[1]] = 'V'
#     # print('\n'.join([''.join(row) for row in grid1]))
#     print(routes)
#     return [len(route)-1 for route in routes]

def find_break(bytes, size):
    start, end = 1, len(bytes)
    middle = (end+start)//2
    while True:
        first = move(bytes, size, middle)
        if not first:
            end = middle
            middle = (end+start)//2
        next = move(bytes, size,  middle+1)
        if not next:
            return bytes[middle]
        start = middle
        middle = (end+start)//2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 18/test.txt')
    input_real = read_file('Day 18/input.txt')
    print('Task1 on test1:', move(input_test, 7, 12))
    print('Task1 on input:', move(input_real, 71, 1024))
    # print('Task2 on test1:', find_break(input_test, 7))
    # print('Task2 on test1:', find_break(input_real, 71))

