def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return {(i, j): el for i, line in enumerate(file)
                for j, el in enumerate(line.strip())}


def should_join(set1, set2):
    for (x1, y1) in set1:
        for (x2, y2) in set2:
            if x1 == x2 and abs(y1 - y2) == 1:
                return True
            if y1 == y2 and abs(x1 - x2) == 1:
                return True
    return False


def join_all_sets(sets_list):
    merged = True
    while merged:
        merged = False
        new_list = []
        used = set()

        for i, lst1 in enumerate(sets_list):
            if i in used:
                continue
            for j, lst2 in enumerate(sets_list[i+1:], start=i+1):
                if j in used:
                    continue
                if should_join(lst1, lst2):
                    new_list.append(lst1 | lst2)
                    used |= {i, j}
                    merged = True
                    break
            else:
                new_list.append(lst1)
        
        sets_list = new_list
    return sets_list


def find_regions(dct):
    regions = {}
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    for coord, letter in sorted(dct.items()):
        if letter not in regions:
            regions[letter] = [{coord}]
        else:
            for regs in regions[letter]:
                if any((coord[0] + dx, coord[1] + dy) in regs for dx, dy in directions):
                    regs.add(coord)
                    break
            else:
                regions[letter].append({coord})
    for letter in regions:
        regions[letter] = join_all_sets(regions[letter])

    return [(letter, reg) for letter, regs in regions.items() for reg in regs]


def main(lst):
    area_per = [
        (letter, len(region), sum(
            ((x, y+1) not in region) + ((x, y-1) not in region) 
            + ((x-1, y) not in region) + ((x+1, y) not in region)
            for (x, y) in region
        ))
        for letter, region in lst
    ]

    return sum(area * per for _, area, per in area_per)


def main2(lst):
    boundaries = []
    for (letter, region) in lst:
        if len(region) == 1:
            boundaries.append((letter, 4, len(region)))
            continue
        sides = 0
        for (x, y) in region:
            sides_per = ((x, y+1) not in region) + ((x, y-1) not in region) + ((x-1, y) not in region) + ((x+1, y) not in region)
            if sides_per == 3:
                sides += 2
                continue
            neighbors = {
                'up': (x, y+1) in region,
                'down': (x, y-1) in region,
                'left': (x-1, y) in region,
                'right': (x+1, y) in region,
                'not_down_right': (x+1, y-1) not in region,
                'not_down_left': (x-1, y-1) not in region,
                'not_up_right': (x+1, y+1) not in region,
                'not_up_left': (x-1, y+1) not in region,
            }
            if not neighbors['up'] and neighbors['down'] and not neighbors['left'] and neighbors['right']:
                sides += 1 + neighbors['not_down_right']
            elif not neighbors['up'] and neighbors['down'] and neighbors['left'] and not neighbors['right']:
                sides += 1 + neighbors['not_down_left']
            elif neighbors['up'] and not neighbors['down'] and not neighbors['left'] and neighbors['right']:
                sides += 1  + neighbors['not_up_right']
            elif neighbors['up'] and not neighbors['down'] and neighbors['left'] and not neighbors['right']:
                sides += 1 + neighbors['not_up_left']
            elif neighbors['up'] and neighbors['down'] and neighbors['left'] and neighbors['right']:
                sides += neighbors['not_down_right'] + neighbors['not_down_left'] + neighbors['not_up_right'] + neighbors['not_up_left']
            elif neighbors['up'] and neighbors['down'] and not neighbors['left'] and neighbors['right']:
                sides += neighbors['not_up_right'] + neighbors['not_down_right']
            elif neighbors['up'] and neighbors['down'] and neighbors['left'] and not neighbors['right']:
                sides += neighbors['not_down_left'] + neighbors['not_up_left']
            elif not neighbors['up'] and neighbors['down'] and neighbors['left'] and neighbors['right']:
                sides += neighbors['not_down_right'] + neighbors['not_down_left']
            elif neighbors['up'] and not neighbors['down'] and neighbors['left'] and neighbors['right']:
                sides += neighbors['not_up_right'] + neighbors['not_up_left']

        boundaries.append((letter, sides, len(region)))
    return  sum(side*area for _, side, area in boundaries)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 12/test.txt')
    # input_test21 = read_file('Day 12/test21.txt')
    input_test2 = read_file('Day 12/test2.txt')
    input_test3 = read_file('Day 12/test3.txt')
    input_test4 = read_file('Day 12/test4.txt')
    input_test5 = read_file('Day 12/test5.txt')
    input_real = read_file('Day 12/input.txt')
    print('Task1 on test:', main(find_regions(input_test)))
    # print('Task1 on test21:', main(find_regions(input_test21)))
    print('Task1 on test2:', main(find_regions(input_test2)))
    print('Task1 on test3:', main(find_regions(input_test3)))
    print('Task1 on input:', main(find_regions(input_real)))
    print('Task2 on test:', main2(find_regions(input_test)))
    print('Task2 on test2:', main2(find_regions(input_test2)))
    print('Task2 on test4:', main2(find_regions(input_test4)))
    print('Task2 on test5:', main2(find_regions(input_test5)))
    print('Task2 on input:', main2(find_regions(input_real)))