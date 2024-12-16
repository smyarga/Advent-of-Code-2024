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


def move(board, start, end):
    paths = {(start, (0, 1)): ({start}, 0)}
    routes = []
    while paths:
        for (end_point, cur_dir), (path, points) in paths.copy().items():
            # print(len(path), end=' ', flush=True)
            del paths[(end_point, cur_dir)]
            px, py = end_point
            if (px, py) == end:
                routes.append((path, end_point, cur_dir, points))
                continue
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newx, newy = px+dx, py+dy
                if (newx, newy) in board and board[(newx, newy)] != '#' and (newx, newy) not in path:
                    path_new = path | {(newx, newy)}
                    new_points = points + (1001 if cur_dir != (dx, dy) else 1)
                    if ((newx, newy), (dx, dy)) not in paths or paths[((newx, newy), (dx, dy))][1] > new_points:
                        paths[((newx, newy), (dx, dy))] = (path_new, new_points)
                    elif paths[((newx, newy), (dx, dy))][1] == new_points:
                        paths[((newx, newy), (dx, dy))] = (paths[((newx, newy), (dx, dy))][0]|path_new, new_points)
    best_routes = [route for route in routes if min(routes, key=lambda x: x[-1])[-1] == route[-1]]
    comf_points = {point for route in best_routes for point in route[0]}
    return sorted(routes, key=lambda x: x[-1])[0][-1], len(comf_points)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test1 = read_file('Day 16/test1.txt')
    input_test2 = read_file('Day 16/test2.txt')
    input_real = read_file('Day 16/input.txt')
    print('Task on test1:', move(*input_test1))
    print('Task on test2:', move(*input_test2))
    print('Task on input:', move(*input_real))