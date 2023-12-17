input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


def decode(input):
    result = []
    group = []
    for line in input.split('\n'):
        if not line:
            if group:
                result.append(group)
            continue
        group.append(line)
    return result

def summarize(input):
    groups = decode(input)
    result = 0
    for group in groups:
        result += find_vertical_line(group)
        result += 100 * find_horizontal_line(group)
    return result

def find_vertical_line(group):
    j = 0
    while j + 1 < len(group[0]):
        
        

            


        
    