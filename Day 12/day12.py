from itertools import product
import math

def should_join(set1, set2):
    for (x1, y1) in set1:
        for (x2, y2) in set2:
            if x1 == x2 and abs(y1 - y2) == 1:
                return True
            if y1 == y2 and abs(x1 - x2) == 1:
                return True
    return False

def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        return {(i, j): el for i, line in enumerate(file)
                for j, el in enumerate(line.strip())}


def join_all_sets(sets_list):
    merged = True
    while merged:
        merged = False
        new_list = []
        used = [False] * len(sets_list)

        for i, lst1 in enumerate(sets_list):
            if used[i]:
                continue
            for j, lst2 in enumerate(sets_list[i+1:], start=i+1):
                if used[j]:
                    continue
                if should_join(lst1, lst2):
                    combined = lst1.union(lst2)
                    new_list.append(combined)
                    used[i] = True
                    used[j] = True
                    merged = True
                    break
            if not used[i]:
                new_list.append(lst1)
        
        sets_list = new_list
    return sets_list

def find_regions(dct):
    regions = {}
    directions = {(-1, 0), (0, 1), (0, -1), (1, 0)}
    for coord, letter in sorted(dct.items()):
        if letter not in regions:
            regions[letter] = [{coord}]
            continue
        for regs in regions[letter]:
            if any(coord == (coor_x+dx, coor_y+dy) for (coor_x, coor_y) in regs for dx, dy in directions):
                regs.add(coord)
                break
        else:
            regions[letter].append({coord})
    for letter, regs in regions.items():
        regions[letter] = join_all_sets(regs)

    return [(letter, reg) for letter, regs in regions.items() for reg in regs]


def main(lst):
    area_per = []
    bound = []
    for (letter, region) in lst:
        area = len(region)
        boundary = set()
        perimeter = 0
        for (x, y) in region:
            sides = ((x, y+1) not in region) + ((x, y-1) not in region) + ((x-1, y) not in region) + ((x+1, y) not in region)
            perimeter += sides
            boundary.add((x, y))

        area_per.append((letter, area, perimeter))
        bound.append((letter, boundary))

    cost = [(key, area*per) for key, area, per in area_per]
    return sum(res for _, res in cost)

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
            if ((x, y+1) not in region) and ((x, y-1) in region) and ((x-1, y) not in region) and ((x+1, y) in region):
                sides += 1 + ((x+1, y-1) not in region)
            if ((x, y+1) not in region) and ((x, y-1) in region) and ((x-1, y) in region) and ((x+1, y) not in region):
                sides += 1 + ((x-1, y-1) not in region)
            if ((x, y+1) in region) and ((x, y-1) not in region) and ((x-1, y) not in region) and ((x+1, y) in region):
                sides += 1  + ((x+1, y+1) not in region)
            if ((x, y+1) in region) and ((x, y-1) not in region) and ((x-1, y) in region) and ((x+1, y) not in region):
                sides += 1 + ((x-1, y+1) not in region)
            if ((x, y+1) in region) and ((x, y-1) in region) and ((x-1, y) in region) and ((x+1, y) in region):
                sides += ((x-1, y+1) not in region) + ((x+1, y+1) not in region) + ((x-1, y-1) not in region) + ((x+1, y-1) not in region)
            if ((x, y+1) in region) and ((x, y-1) in region) and ((x-1, y) not in region) and ((x+1, y) in region):
                sides += ((x+1, y+1) not in region) +  ((x+1, y-1) not in region)
            if ((x, y+1) in region) and ((x, y-1) in region) and ((x-1, y) in region) and ((x+1, y) not in region):
                sides += ((x-1, y+1) not in region) +  ((x-1, y-1) not in region)
            if ((x, y+1) not in region) and ((x, y-1) in region) and ((x-1, y) in region) and ((x+1, y) in region):
                sides += ((x+1, y-1) not in region) +  ((x-1, y-1) not in region)
            if ((x, y+1) in region) and ((x, y-1) not in region) and ((x-1, y) in region) and ((x+1, y) in region):
                sides += ((x+1, y+1) not in region) +  ((x-1, y+1) not in region)

        boundaries.append((letter, sides, len(region)))
    return boundaries, sum(side*area for _, side, area in boundaries)

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
    # print('Task1 on test:', main(find_regions(input_test)))
    # # print('Task1 on test21:', main(find_regions(input_test21)))
    # print('Task1 on test2:', main(find_regions(input_test2)))
    # print('Task1 on test3:', main(find_regions(input_test3)))
    # print('Task1 on input:', main(find_regions(input_real)))
    print('Task2 on test2:', main2(find_regions(input_test)))
    print('Task2 on test2:', main2(find_regions(input_test2)))
    print('Task2 on test4:', main2(find_regions(input_test4)))
    print('Task2 on test4:', main2(find_regions(input_test5)))
    print('Task2 on input:', main2(find_regions(input_real)))