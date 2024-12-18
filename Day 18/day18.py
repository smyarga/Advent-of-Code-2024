def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

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
    while paths and not routes:
        for end_point, path in paths.copy().items():
            del paths[end_point]
            px, py = end_point
            if (px, py) == end:
                routes.append((path, end_point))
                continue
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newx, newy = px+dx, py+dy
                if (newx, newy) in grid and grid[(newx, newy)] != '#' and (newx, newy) not in path:
                    path_new = path | {(newx, newy)}
                    if ((newx, newy), (dx, dy)) not in paths:
                        paths[(newx, newy)] = path_new

    return [len(route[0])-1 for route in routes]


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
    print('Task2 on test1:', find_break(input_test, 7))
    print('Task2 on test1:', find_break(input_real, 71))


# def move(bytes, size, steps):
#     start = (0, 0)
#     end = (size-1, size-1)
#     grid = {(i, j): '.' for i in range(size) for j in range(size)}
#     for (bx, by) in bytes[:steps]:
#         grid[(by, bx)] = '#'
#     grid1 = [[None]*(size) for _ in range(size)]
#     for key, val in grid.items():
#         grid1[key[0]][key[1]] = val
#     print('\n'.join([''.join(row) for row in grid1]))
#     paths = {start: [start]}
#     routes = []
#     while paths and not routes:
#         for end_point, path in paths.copy().items():
#             # print( end_point, path)
#             # print(len(path), end=' ', flush=True)
#             del paths[end_point]
#             px, py = end_point
#             if (px, py) == end:
#                 routes.append((path, end_point))
#                 continue
#             while True:
#                 print('!', px, py)
#                 pos_ways = []
#                 for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
#                     newx, newy = px+dx, py+dy
#                     if (newx, newy) in grid and grid[(newx, newy)] != '#' and (newx, newy) not in path:
#                         path_new = path + [(newx, newy)]
#                         pos_ways.append(((newx, newy), path_new))
#                 if len(pos_ways) != 1:
#                     break
#                 (px, py), path = pos_ways[0]
            
#             if pos_ways:
#                 # print((newx, newy), pos_ways)
#                 for ((newx, newy), path_new) in pos_ways:
#                     if ((newx, newy), (dx, dy)) not in paths:
#                         paths[(newx, newy)] = path_new
#     # for key in routes[0][0]:
#     #     grid1[key[0]][key[1]] = 'V'
#     # print('\n'.join([''.join(row) for row in grid1]))
#     return [len(route[0])-1 for route in routes]