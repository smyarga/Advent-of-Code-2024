from math import log10
from collections import defaultdict

def read_file(pathname: str) -> dict[tuple[int, int], str]:
    """
    Reads a file and converts its content into a dictionary.
    """
    with open(pathname, 'r', encoding='utf-8') as file:
        stones = tuple(map(int, file.read().strip().split()))
        return {el: stones.count(el) for el in stones}


def split_n(el):
    num_digits = int(log10(el)) + 1
    if num_digits % 2 == 0:
        half = num_digits // 2
        div = 10 ** half
        return [el // div, el % div]
    return None


def blink(el):
    if el == 0:
        return [1]
    new = split_n(el)
    if new:
        return new
    return [el*2024]

def update(row):
    new_stones = defaultdict(int)
    for el, n in row.items():
        for stone in blink(el):
            new_stones[stone] += n
    return new_stones

def main(row, blinks):
    for _ in range(blinks):
        row = update(row)
    return row




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    input_test = read_file('Day 11/test.txt')
    input_test2 = read_file('Day 11/test2.txt')
    input_real = read_file('Day 11/input.txt')
    print('Task1 on test:', main(input_test, 1))
    print('Task1 on test2:', sum(main(input_test2, 6).values()))
    print('Task1 on input:', sum(main(input_real, 25).values()))
    print('Task1 on input:', sum(main(input_real, 75).values()))



# def blink(el, blinks):
#     if blinks == 0:
#         return (el,)
#     if el == 0:
#         return blink(1, blinks-1)
#     new = split_n(el)
#     if new:
#         return blink(new[0], blinks-1) + blink(new[1], blinks-1)
#     return blink(el*2024, blinks-1)

# def main(row, blinks):
#     blinked = []
#     for i, el in enumerate(row):
#         print(i, flush=True)
#         blinked.append(blink(el, blinks) )
#     return [el for lst in blinked for el in lst]