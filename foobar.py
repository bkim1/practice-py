import math
def answer(area):
    blocks = [] 
    remaining_area = area
    while remaining_area > 0:
        biggest_square = int(math.sqrt(remaining_area))
        blocks.append(biggest_square)
        remaining_area -= biggest_square ** 2
    print(blocks)
    return blocks

print(answer(12))
print(answer(15324))