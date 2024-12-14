def read_file(pathname: str) -> list:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        result = []
        max_x = 0
        max_y = 0
        for line in file:
            p, v = line.strip().split()
            p = tuple(map(int, p.split('=')[1].split(',')))
            if p[0] > max_x:
                max_x = p[0]
            if p[1] > max_y:
                max_y = p[1]
            v = tuple(map(int, v.split('=')[1].split(',')))
            result.append((p, v))
        return result, (max_x+1, max_y+1)


def main(robots):
    robots, size = robots
    grid = [[0]*size[0] for _ in  range(size[1])]
    for i in range(101):
        for (p_x, p_y), (v_x, v_y) in robots:
            if grid[(p_y+v_y*i)%size[1]][(p_x+v_x*i)%size[0]] == 0:
                grid[(p_y+v_y*i)%size[1]][(p_x+v_x*i)%size[0]] = 1
            else:
                grid[(p_y+v_y*i)%size[1]][(p_x+v_x*i)%size[0]] += 1
            if i!=0:
                grid[(p_y+v_y*(i-1))%size[1]][(p_x+v_x*(i-1))%size[0]] -= 1
    if size[1] % 2:
        grid1, grid2 = grid[:size[1]//2], grid[size[1]//2+1:]
    else:
        grid1, grid2 = grid[:size[1]//2-1], grid[size[1]//2-1:]
    if size[0] % 2:
        grid11 = [row[:size[0]//2] for row in grid1]
        grid12 = [row[size[0]//2+1:] for row in grid1]
        grid21 = [row[:size[0]//2] for row in grid2]
        grid22 = [row[size[0]//2+1:] for row in grid2]
    else:
        grid11 = [row[:size[0]//2-1] for row in grid1]
        grid12 = [row[size[0]//2-1:] for row in grid1]
        grid21 = [row[:size[0]//2-1] for row in grid2]
        grid22 = [row[size[0]//2-1:] for row in grid2]
    result = sum(sum(row) for row in grid11)*sum(sum(row) for row in grid12)*sum(sum(row) for row in grid21)*sum(sum(row) for row in grid22)
    return result


def main2(robots):
    robots, size = robots
    grid = [[0]*size[0] for _ in  range(size[1])]
    for i in range(size[0]*size[1]):
        for (p_x, p_y), (v_x, v_y) in robots:
            if grid[(p_y+v_y*i) % size[1]][(p_x+v_x*i) % size[0]] == 0:
                grid[(p_y+v_y*i) % size[1]][(p_x+v_x*i) % size[0]] = 1
            else:
                grid[(p_y+v_y*i) % size[1]][(p_x+v_x*i) % size[0]] += 1
            if i != 0:
                grid[(p_y+v_y*(i-1))%size[1]][(p_x+v_x*(i-1))%size[0]] -= 1
        grid1 = [''.join('*' if c else ' ' for c in row) for row in grid]
        print(i, end='\r', flush=True)
        if any('**********' in row for row in grid1):
            print(i)
            break
    return '\n'.join(grid1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 14/test copy.txt')
    input_real = read_file('Day 14/input.txt')
    print('Task1 on test:', main(input_test))
    print('Task1 on input:', main(input_real))
    print('Task2 on test:', main2(input_real))