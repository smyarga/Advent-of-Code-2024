def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return {(i, j): int(el) for i, line in enumerate(file)
                for j, el in enumerate(line.strip())}

def main(dct):
    count1 = 0
    count2 = 0
    start_points = set()
    for key, val in dct.items():
        if val == 0:
            start_points.add(key)
    directions = {(-1, 0), (0, 1), (0, -1), (1, 0)}
    for s_x, s_y in start_points:
        paths = [[(s_x, s_y)]]
        cur = 0
        while cur < 9:
            for i, path in enumerate(paths.copy()):
                paths.remove(path)
                cur_x, cur_y = path[-1]
                for dx, dy in directions:
                    if dct.get((cur_x + dx, cur_y + dy), '') == cur+1:
                        paths.append(path+[(cur_x + dx, cur_y + dy)])
            
            cur += 1
        
        count1 += len({path[-1] for path in paths})
        count2 += len(paths)

    return count1, count2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 10/test.txt')
    input_real = read_file('Day 10/input.txt')
    print('Task1 on test:', main(input_test))
    print('Task1 on input:', main(input_real))
