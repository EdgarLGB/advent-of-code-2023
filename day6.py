import math
from dataclasses import dataclass
import re
input = """
Time:        47     70     75     66
Distance:   282   1079   1147   1062
"""

input2 = """
Time:      7  15   30
Distance:  9  40  200
"""


def extract_digits(input):
    return list(map(lambda x: int(x), re.findall('\d+', input)))


@dataclass
class Game:
    time_list: []
    distance_list: []


def decode(input):
    two_parts = input.split('\n')
    time_list = extract_digits(two_parts[1])
    distance_list = extract_digits(two_parts[2])
    return Game(time_list, distance_list)


a = 1    # accelaration = 1 mm/ms2


def get_number_of_beaten_list(game):
    for i in range(len(game.time_list)):
        t = game.time_list[i]
        d = game.distance_list[i]
        beaten_times = 0
        for t_1 in range(t + 1):
            t_2 = t - t_1
            actual_distance = a * t_1 * t_2
            if actual_distance > d:
                beaten_times += 1
        yield beaten_times


def calculate_number_of_ways(input):
    game = decode(input)
    number_of_beaten_list = get_number_of_beaten_list(game)
    return math.prod(number_of_beaten_list)


print(calculate_number_of_ways(input))

###### Part two ######


@dataclass
class Game2:
    time: int
    distance: int


def extract_number_from_bad_kerning_str(input):
    return int(''.join(re.findall('\d+', input)))


def decode_2(input):
    two_parts = input.split('\n')
    time = extract_number_from_bad_kerning_str(two_parts[1])
    distance = extract_number_from_bad_kerning_str(two_parts[2])
    return Game2(time, distance)


def calculate_beaten_ways(input):
    game = decode_2(input)
    # Use quadratic equation solution
    partial_solution = math.pow(
        math.pow(game.time, 2) - 4 * game.distance, 0.5)
    t_solution_lower_bound = (game.time - partial_solution) / 2
    t_solution_upper_bound = (game.time + partial_solution) / 2
    intersection_lower_bound = math.ceil(max(0, t_solution_lower_bound))
    intersection_upper_bound = math.floor(
        min(game.time, t_solution_upper_bound))
    return intersection_upper_bound - intersection_lower_bound + 1


print(calculate_beaten_ways(input))
