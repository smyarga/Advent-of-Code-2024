def read_file(pathname: str) -> list:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        grid = {}
        directions = ''
        for i, line in enumerate(file):
            line = line.strip()
            if '#' in line:
                grid.update({(i, j): el for j, el in enumerate(line)})
            elif line:
                directions += line
        return grid, directions


def main(grid, directions):
    print(directions)
    rows, columns = zip(*grid)
    height, width = max(rows), max(columns)
    print(height, width)
    dirs= {'v': (1, 0), '>': (0, 1), '<': (0, -1), '^': (-1, 0)}
    for key, val in grid.items():
        if val == '@':
            s_x, s_y = key
    for dir in directions:
        x, y = dirs[dir]
        new_x, new_y = x + s_x, y + s_y
        # print(dir, new_x, new_y)
        if grid[(new_x, new_y)] == '.':
            grid[(new_x, new_y)] = '@'
            grid[(s_x, s_y )] = '.'
            s_x, s_y = new_x, new_y
        elif grid[(new_x, new_y)] == '#':
            continue
        else:
            i = 2
            while True:
                if grid[s_x + x*i, s_y + y*i] == '#':
                    break
                if grid[s_x + x*i, s_y + y*i] == 'O':
                    i += 1
                    continue
                if grid[s_x + x*i, s_y + y*i] == '.':
                    grid[(new_x, new_y)] = '@'
                    for k in range(2, i+1):
                        # print(k, s_x, s_y, s_x + x*k, s_y + y*k)
                        grid[s_x + x*k, s_y + y*k] = 'O'                  
                    grid[(s_x, s_y )] = '.'
                    s_x, s_y = new_x, new_y
                    break


        # grid1 = [[None]*(width+1) for _ in range(height+1)]
        # for key, val in grid.items():
        #     grid1[key[0]][key[1]] = val
        # print('\n'.join([''.join(row) for row in grid1]))
    result = 0
    for (x, y), val in grid.items():
        if val == 'O':
            result += 100*x+y

    return grid, result

def wide_map(pathname):
    new_map = []
    directions = ''
    with open(pathname, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            new_line = ''
            if '#' in line:
                for el in line:
                    if el in ['#', '.']:
                        new_line += el*2
                    elif el == 'O':
                        new_line += '[]'
                    elif el == '@':
                        new_line += '@.'
                new_map.append(new_line)
            elif line:
                directions += line
    print('\n'.join([''.join(row) for row in new_map]))
    map_ = {}
    for i, row in enumerate(new_map):
        for j, el in enumerate(row):
            map_[(i, j)] = el

    return map_, directions


def main2(grid, directions):
    print(directions)
    rows, columns = zip(*grid)
    height, width = max(rows), max(columns)
    print(height, width)
    dirs= {'v': (1, 0), '>': (0, 1), '<': (0, -1), '^': (-1, 0)}
    for key, val in grid.items():
        if val == '@':
            s_x, s_y = key
    for dir in directions:
        x, y = dirs[dir]
        new_x, new_y = x + s_x, y + s_y
        # print(new_x, new_y, s_x, s_y, end=' ')
        # print(dir, new_x, new_y, end=' ')
        if grid[(new_x, new_y)] == '.':
            grid[(new_x, new_y)] = '@'
            grid[(s_x, s_y)] = '.'
            s_x, s_y = new_x, new_y
        elif grid[(new_x, new_y)] == '#':
            continue
        else:
            if dir in '><':
                i = 2
                cur = grid[(new_x, new_y)]
                while True:
                    if grid[s_x + x*i, s_y + y*i] == '#':
                        break
                    if grid[s_x + x*i, s_y + y*i] in '[]':
                        i += 1
                        continue
                    if grid[s_x + x*i, s_y + y*i] == '.':
                        grid[(new_x, new_y)] = '@'
                        for k in range(2, i+1):
                            grid[s_x + x*k, s_y + y*k] = cur if k%2 == 0 else ('[' if cur==']' else ']')
                        grid[(s_x, s_y)] = '.'
                        s_x, s_y = new_x, new_y
                        break
            else:
                i = 1
                to_check = [[(s_x + x, s_y + y)]]
                while True:
                    if any(grid[coord] == '#' for coord in to_check[-1]):
                        break
                    if any(grid[coord] in '[]' for coord in to_check[-1]):
                        new_check = []
                        for coord in to_check[-1]:
                            if grid[coord] == '[':
                                new_check += [coord, (coord[0], coord[1]+1)]
                            elif grid[coord] == ']':
                                new_check += [coord, (coord[0], coord[1]-1)]
                            # else:
                            #     new_check += [coord]
                        i += 1
                        to_check.append([(newx+x, newy+y) for newx, newy in set(new_check)])
                        continue
                    if all(grid[coord] == '.' for coord in to_check[-1]):
                        for layer in to_check[::-1]:
                            for cx, cy in layer:
                                grid[(cx, cy)] = grid[(cx - x, cy)]
                                grid[(cx - x, cy)] = '.'
                            # if (new_x, new_y) == (6, 3):
                            #     grid1 = [[None]*(width+1) for _ in range(height+1)]
                            #     for key, val in grid.items():
                            #         grid1[key[0]][key[1]] = val
                            #     print('\n'.join([''.join(row) for row in grid1]))
                        s_x, s_y = new_x, new_y
                        break

        with open('result.txt', 'w+') as file:
            grid1 = [[None]*(width+1) for _ in range(height+1)]
            for key, val in grid.items():
                grid1[key[0]][key[1]] = val
            print(dir, new_x, new_y, file=file)
            print('\n'.join([''.join(row) for row in grid1]), file=file)
    result = 0
    for (x, y), val in grid.items():
        if val == '[':
            result += 100*x+y

    return grid, result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test1 = read_file('Day 15/test1.txt')
    input_test = read_file('Day 15/test.txt')
    input_test3 = read_file('Day 15/test3.txt')
    input_real = read_file('Day 15/input.txt')
    print('Task1 on test:', main(*input_test1))
    print('Task1 on test:', main(*input_test))
    print('Task1 on input:', main(*input_real))
    print('Task1 on test:', wide_map('Day 15/test.txt'))
    print('Task1 on test:', wide_map('Day 15/test3.txt'))
    # print('Task1 on test:', main2(*wide_map('Day 15/test3.txt')))
    print('Task1 on test:', main2(*wide_map('Day 15/test.txt')))
    print('Task1 on test:', main2(*wide_map('Day 15/input.txt')))