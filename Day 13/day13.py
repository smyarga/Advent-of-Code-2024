def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        output = []
        play = {}
        for line in file:
            if 'Button' in line:
                _, letter, x, y = line.strip().split()
                play[letter[:-1]] = (int(x[:-1].split('+')[1]), int(y.split('+')[1]))
            elif 'Prize' in line:
                _, x, y = line.strip().split()
                play['Prize'] = (int(x[:-1].split('=')[1]), int(y.split('=')[1]))
                output.append(play)
                play = {}
        return output


def win_prize(case, limit=0):
    '''
    >>> win_prize({'A': (94, 34), 'B': (22, 67), 'Prize': (8400, 5400)})
    280
    >>> win_prize({'A': (26, 66), 'B': (67, 21), 'Prize': (12748, 12176)})
    0
    >>> win_prize({'A': (17, 86), 'B': (84, 37), 'Prize': (7870, 6450)})
    200
    >>> win_prize({'A': (69, 23), 'B': (27, 71), 'Prize': (18641, 10279)})
    0
    '''
    det = -case['A'][0]* case['B'][1] + case['A'][1]* case['B'][0]
    if det == 0:
        return 0
    x = (case['Prize'][0] * case['A'][1] - case['Prize'][1] * case['A'][0])/det
    y = (case['Prize'][1] * case['B'][0] - case['Prize'][0] * case['B'][1])/det
    if int(x) == x and int(y) == y and (min(x, y) <= limit if limit else True):
        return int(x+3*y)
    return 0


def main(plays):
    part1 = sum(win_prize(case, 100) for case in plays)
    for case in plays:
        x, y = case['Prize']
        case['Prize'] = (x+10000000000000, y+10000000000000)
    part2 = sum(win_prize(case) for case in plays)
    return part1, part2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 13/test.txt')
    input_test2 = read_file('Day 13/test2.txt')
    input_real = read_file('Day 13/input.txt')
    print('Task1 on test:', main(input_test))
    print('Task1 on input:', main(input_real))
    print('Task2 on test:', main(input_test2))
