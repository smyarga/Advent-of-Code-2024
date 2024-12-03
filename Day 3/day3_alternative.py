from re import findall

total1 = total2 = 0
enabled = True
with open('test1.txt', 'r', encoding='utf-8') as file:
    data = file.read()
print(findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data))


for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    print(a, b, do, dont)
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        total1 += x
        total2 += x * enabled

print(total1, total2)