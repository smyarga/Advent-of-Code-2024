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
        board = {}
        for i, line in enumerate(file):
            for j, el in enumerate(line.strip()):
                board[(i, j)] = el
                if el == 'S':
                    start = (i, j)
                elif el == 'E':
                    end = (i, j)
        return board, start, end

# @timeit
# def move(board, start, end):
#     paths = {(start, (0, 1)): ({start}, 0)}
#     routes = []
#     while paths:
#         for (end_point, cur_dir), (path, points) in paths.copy().items():
#             # print(len(path), end=' ', flush=True)
#             del paths[(end_point, cur_dir)]
#             px, py = end_point
#             if (px, py) == end:
#                 routes.append((path, end_point, cur_dir, points))
#                 continue
#             for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
#                 newx, newy = px+dx, py+dy
#                 if (newx, newy) in board and board[(newx, newy)] != '#' and (newx, newy) not in path:
#                     path_new = path | {(newx, newy)}
#                     new_points = points + (1001 if cur_dir != (dx, dy) else 1)
#                     if ((newx, newy), (dx, dy)) not in paths or paths[((newx, newy), (dx, dy))][1] > new_points:
#                         paths[((newx, newy), (dx, dy))] = (path_new, new_points)
#                     elif paths[((newx, newy), (dx, dy))][1] == new_points:
#                         paths[((newx, newy), (dx, dy))] = (paths[((newx, newy), (dx, dy))][0]|path_new, new_points)
#     best_routes = [route for route in routes if min(routes, key=lambda x: x[-1])[-1] == route[-1]]
#     comf_points = {point for route in best_routes for point in route[0]}
#     return sorted(routes, key=lambda x: x[-1])[0][-1], len(comf_points)

@timeit
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
            while True:
                pos_ways = []
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    newx, newy = px+dx, py+dy
                    if (newx, newy) in board and board[(newx, newy)] != '#' and (newx, newy) not in path:
                        path_new = path | {(newx, newy)}
                        new_points = points + (1001 if cur_dir != (dx, dy) else 1)
                        pos_ways.append(((newx, newy), path_new, new_points))
                # if len(pos_ways) == 1 and board[(newx, newy)] == 'E':
                #     break
                if len(pos_ways) == 1:
                    path = path_new
                    points = new_points
                else:
                    break
            if not pos_ways:
                continue
            for ((newx, newy), path_new, new_points) in pos_ways:
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
    # print('Task on test2:', move(*input_test2))
    # print('Task on input:', move(*input_real))





# @timeit
# def move(board, start, end):
#     paths = {(start, (0, 1)): ({start}, 0)}
#     routes = []
#     while paths:
#         ((px, py), cur_dir), (path, points) = paths.popitem()
#         min_dist = abs(px-end[0]) + abs(py-end[1]) + (1000 if px != end[0] or py != end[1] else 0)
#         if (px, py) == end:
#             routes.append((path, (px, py), cur_dir, points))
#             continue
#         for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#             newx, newy = px+dx, py+dy
#             if board.get((newx, newy), '') in ['.', 'E'] and (newx, newy) not in path:
#                 new_points = points + (1001 if cur_dir != (dx, dy) else 1)
#                 current_path_info = paths.get(((newx, newy), (dx, dy)), (None, float('inf')))
#                 if current_path_info[1] + min_dist > new_points:
#                     paths[((newx, newy), (dx, dy))] = (path | {(newx, newy)}, new_points)
#                 elif current_path_info[1] == new_points:
#                     current_path_info[0].update(path)
#     best_routes = [route for route in routes if min(routes, key=lambda x: x[-1])[-1] == route[-1]]
#     comf_points = {point for route in best_routes for point in route[0]}
#     return sorted(routes, key=lambda x: x[-1])[0][-1], len(comf_points)