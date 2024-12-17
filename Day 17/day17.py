def calculate(a: int, b: int, c: int, program: str):
    '''
    >>> calculate(None, None, 9, '2,6')
    (None, 1, 9, '')
    >>> calculate(10, None, None, '5,0,5,1,5,4')
    (10, None, None, '0,1,2')
    >>> calculate(2024, None, None, '0,1,5,4,3,0')
    (0, None, None, '4,2,5,6,7,7,7,7,3,1,0')
    >>> calculate(None, 29, None, '1,7')
    (None, 26, None, '')
    >>> calculate(None, 2024, 43690, '4,0')
    (None, 44354, 43690, '')
    >>> calculate(729, 0, 0, '0,1,5,4,3,0')
    (0, 0, 0, '4,6,3,5,6,3,5,2,1,0')
    '''
    output = []
    dct_instr = {'0': 'adv', '1': 'bxl', '2': 'bst', '3': 'jnz',
                '4': 'bxc', '5': 'out', '6': 'bdv', '7': 'cdv'}
    data = program.split(',')
    i = 0
    while i in range(len(data)):
        combo = {'0': 0, '1': 1, '2': 2, '3': 3,
             '4': a, '5': b, '6': c}
        match dct_instr[data[i]], data[i+1]:
            case 'adv', op:
                a = a >> combo[op]
            case 'bxl', op:
                b = b ^ int(op)
            case 'bst', op:
                b = combo[op] % 8
            case 'jnz', op:
                if a == 0:
                    pass
                else:
                    i = int(op) - 2
            case 'bxc', op:
                b = b ^ c
            case 'out', op:
                output.append(str(combo[op] % 8))
            case 'bdv', op:
                b = a >> combo[op]
            case 'cdv', op:
                c = a >> combo[op]
        i += 2

    result = (a, b, c, ','.join(output))
    # print(operands, instructions)
    return result

def find_lowest(program):
    '''
    >>> find_lowest('0,3,5,4,3,0')
    117440
    '''
    program_splitted = program.split(',')
    # for i in range(50):
    #     print(calculate(i, 0, 0, program))
    ind = [(0, len(program_splitted)-1)]

    while True:
        start, index = ind.pop(0)
        for i in range(start*8, start*8 + 8):
            if calculate(i, 0, 0, program)[3] == ','.join(program_splitted[index:]):
                ind.append((i, index-1))
                if index == 0:
                    return i


if __name__=='__main__':
    import doctest
    doctest.testmod()
    program = '2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0'
    print(calculate(59397658, 0, 0, program))
    print(find_lowest(program))

