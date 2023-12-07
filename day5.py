import sys
import re
from dataclasses import dataclass
input = """
seeds: 3169137700 271717609 3522125441 23376095 1233948799 811833837 280549587 703867355 166086528 44766996 2326968141 69162222 2698492851 14603069 2755327667 348999531 2600461189 92332846 1054656969 169099767

seed-to-soil map:
404519244 291909660 232498813
1320269465 1130502191 53088254
3383428636 3839037267 267181273
0 667785713 35892165
1373357719 524408473 98619504
2581158120 2457172776 306553547
80649901 971363049 35482565
2330985014 3113014199 250173106
637018057 1006845614 54766591
1010187739 1061612205 68889986
851189485 132911406 158998254
718278079 0 132911406
1079077725 730171309 241191740
2887711667 2392582028 64590748
3321831622 2330985014 61597014
3650609909 4106218540 188748756
2952302415 3363187305 20241331
368073252 1183590445 36445992
3839358665 3383428636 455608631
35892165 623027977 44757736
2972543746 2763726323 349287876
691784648 703677878 26493431
116132466 1220036437 251940786

soil-to-fertilizer map:
1392321439 1575423106 1147080465
261871322 2722503571 622657242
884528564 768981668 507792875
3152000765 0 514557996
2539401904 3607032135 247383303
2786785207 3854415438 110791886
2897577093 514557996 254423672
3666558761 1276774543 298648563
0 3345160813 261871322

fertilizer-to-water map:
385494683 1437201590 374714893
3894452006 2756513635 124929297
1389571244 1299917000 137284590
3267934068 2881442932 9378230
4140946106 2602492445 154021190
760209576 585965354 629361668
1948388381 1832044460 70164711
170741915 176668131 214752768
3570093835 2531499423 70993022
2647843344 3421511423 399466167
1832044460 3124261283 116343921
3458218517 2890821162 111875318
1721400289 1215327022 84589978
1526855834 391420899 194544455
4019381303 3002696480 121564803
3641086857 4041602147 253365149
2018553092 1902209171 629290252
3047309511 3820977590 220624557
1805990267 170741915 5926216
3277312298 3240605204 180906219

water-to-light map:
3186854896 2955619881 216294813
1320085115 3394507929 25016085
1300936985 1818141535 19148130
3620767971 560782805 39686383
2121550779 2395592136 95582251
3594740149 4260270958 26027822
1138228493 3171914694 34259798
823736132 600469188 55727065
3049715340 2803112532 137139556
0 461804882 98977923
2217133030 1416346841 282474073
1225320767 1742525317 75616218
3481284141 3206174492 113456008
1172488291 656196253 52832476
1980983454 2662545207 140567325
182051501 2121838778 15960124
1788572787 256566375 2332800
881662118 0 256566375
3769058535 899106596 517240245
157917514 3851650114 24133987
564440564 1937530266 107354197
2527210819 4090588051 169682907
1790905587 709028729 190077867
2499607103 3824046398 27603716
1585667080 258899175 202905707
671794761 3419524014 51700770
3403149709 2491174387 62766639
228474519 2044884463 76954315
3660454354 2553941026 108604181
305428834 2137798902 257793234
879463197 3875784101 2198921
2696893726 3471224784 352821614
1345101200 3319630500 74877429
98977923 4031648460 58939591
1541962677 1698820914 43704403
3465916348 2940252088 15367793
1419978629 3909664412 121984048
723495531 1837289665 100240601
563222068 3908445916 1218496
198011625 3877983022 30462894

light-to-temperature map:
2138957924 2867100637 394375633
1108145028 3261476270 27971395
2732973434 712143665 259385506
642453123 1589178663 51870752
316125718 164593015 67732689
0 145842404 18750611
1861017768 2758655274 29719920
2130609825 2858752538 8348099
828190830 2187066385 73864838
18750611 0 126160197
144910808 376698573 26842041
383858407 126160197 19682207
2533333557 3337386080 199639877
1507332395 1950588856 215367909
3619117542 3537025957 51848058
1740303803 1763491162 21707209
3793407347 4140330531 154636765
477829952 3588874015 164623171
1722700304 1432603163 17603499
1890737688 493381148 218762517
4255326359 1549537726 39640937
1408001331 1450206662 99331064
2992358940 2260931223 497724051
429891537 3289447665 47938415
3670965600 1641049415 122441747
171752849 232325704 144372869
3504169105 3753497186 114948437
2109500205 2165956765 21109620
4113434597 1290711401 141891762
3490082991 1070535927 14086114
1136116423 3868445623 271884908
757813486 2788375194 70377344
3948044112 1785198371 165390485
694323875 429891537 63489611
1762011012 971529171 99006756
902055668 1084622041 206089360

temperature-to-humidity map:
480269915 557576190 100117705
2489408207 1585236324 410693151
2900101358 422045351 135530839
666327594 779006907 28457451
1945409298 807464358 543998909
96132998 2440771002 3096292
1295929224 2746460169 2283706
1298212930 2022055443 99310345
3547441134 3503466915 344864128
1659646920 325230280 96815071
4125576596 3928494543 169390700
3035632197 1351463267 233773057
1397523275 2592671813 109157546
1032938960 2748743875 109076238
1756461991 2276586008 92935317
3968917823 4097885243 156658773
595077917 2369521325 71249677
1593864657 3027700045 65782263
850005265 657693895 121313012
1506680821 2505487977 87183836
1186646008 0 109283216
1849397308 3389340328 96011990
3496945571 4254544016 40423280
3898826606 3858403326 70091217
99229290 3189615306 199725022
468834244 1995929475 11435671
3269405254 109283216 215947064
580387620 2007365146 14690297
0 3093482308 96132998
971318277 2443867294 61620683
3892305262 3496945571 6521344
298954312 2857820113 169879932
1142015198 2701829359 44630810
694785045 2121365788 155220220
3537368851 3848331043 10072283

humidity-to-location map:
3490144003 1623866227 218040905
1709610578 1620839197 3027030
105449249 586389428 113279526
1899604338 2167886292 348178199
1712637608 2678624215 186966730
218728775 0 245776251
2472992580 923734334 143670388
2616662968 3670169885 15297294
2247782537 1395629154 225210043
0 480940179 105449249
4113852846 3959729057 159909096
3322784653 1067404722 167359350
923734334 4119638153 175329143
1534964496 2516064491 162559724
2631960262 3496028440 140849733
2862695906 1234764072 97988355
1697524220 3636878173 12086358
2985646048 1332752427 62876727
1099063477 2970241510 435901019
4009202281 2865590945 104650565
2960684261 2142924505 24961787
2772809995 3406142529 89885911
4273761942 3648964531 21205354
3708184908 1841907132 301017373
464505026 245776251 235163928
3048522775 3685467179 274261878
"""

input2 = """
seeds: 79 14

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


@dataclass(frozen=True)
class Game:
    seeds: []
    group_of_mappings: []


@dataclass(frozen=True)
class Mapping:
    source: int
    destination: int
    range_length: int


def decode(input):
    lines = input.split('\n')
    seeds = extract_numbers(lines[1])
    all_mappings = []
    partial_mapping = []
    for i in range(3, len(lines)):
        line = lines[i]
        if "map:" in line:
            continue
        elif line == "":
            if len(partial_mapping) == 0:
                continue
            all_mappings.append(partial_mapping)
            partial_mapping = []
        else:
            triple_numbers = extract_numbers(line)
            partial_mapping.append(
                Mapping(triple_numbers[1], triple_numbers[0], triple_numbers[2]))
    return Game(seeds, all_mappings)


def extract_numbers(input):
    return list(map(lambda x: int(x), re.findall('\d+', input)))


def calculate_lowest_location_number(input):
    game = decode(input)
    result = sys.maxsize
    for seed in game.seeds:
        seed = convert_seed(game.group_of_mappings, seed)
        result = min(result, seed)
    return result


def convert_seed(group_of_mappings, seed):
    for group in group_of_mappings:
        for mapping in group:
            delta = seed - mapping.source
            if delta >= 0 and delta < mapping.range_length:
                seed = mapping.destination + delta
                break
    return seed


print(calculate_lowest_location_number(input))

###### Part two ######


@dataclass(frozen=True)
class SeedInterval:
    start: int
    stop: int

@dataclass(frozen=True)
class MappingInterval:
    source_start: int
    source_stop: int
    destination_start: int


def extract_seed_intervals(input):
    numbers = extract_numbers(input)
    for i in range(0, len(numbers), 2):
        yield SeedInterval(numbers[i], numbers[i] + numbers[i + 1] - 1)


def decode_2(input):
    lines = input.split('\n')
    seeds = extract_seed_intervals(lines[1])
    all_mappings = []
    partial_mapping = []
    for i in range(3, len(lines)):
        line = lines[i]
        if "map:" in line:
            continue
        elif line == "":
            if len(partial_mapping) == 0:
                continue
            all_mappings.append(partial_mapping)
            partial_mapping = []
        else:
            triple_numbers = extract_numbers(line)
            partial_mapping.append(
                MappingInterval(triple_numbers[1], triple_numbers[1] + triple_numbers[2] - 1, triple_numbers[0]))
    return Game(seeds, all_mappings)


def convert_seed_interval(seed_interval, group_of_mappings):
    input = [seed_interval]
    for group_of_mapping in group_of_mappings:
        converted_input = []
        for mapping in group_of_mapping:
            difference = mapping.destination_start - mapping.source_start
            unconverted_input = []
            for seed in input:
                has_intersection, intersection_start, intersection_stop = find_intersection(
                    seed.start, seed.stop, mapping.source_start, mapping.source_stop)
                # print(f"start={intersection_start},stop={intersection_stop}")
                if not has_intersection:
                    unconverted_input.append(seed)
                    continue
                if seed.start < intersection_start:
                    unconverted_input.append(
                        SeedInterval(seed.start, intersection_start - 1))
                if intersection_stop < seed.stop:
                    unconverted_input.append(
                        SeedInterval(intersection_stop + 1, seed.stop))
                converted_input.append(
                    SeedInterval(intersection_start + difference, intersection_stop + difference))
                # print(f"unconverted: {unconverted_input}")
                # print(f"converted: {converted_input}")
            input = unconverted_input
        input += converted_input
    print(input)
    return input


def find_intersection(a_start, a_stop, b_start, b_stop):  # all inclusive
    intersection_start = max(a_start, b_start)
    intersection_stop = min(a_stop, b_stop)
    if intersection_start <= intersection_stop:
        return True, intersection_start, intersection_stop
    return False, None, None


def calculate_lowest_location_number_2(input):
    game = decode_2(input)
    converted_seed_range_list = []
    for seed in game.seeds:
        converted_seed_range_list += convert_seed_interval(
            seed, game.group_of_mappings)

    # print(set(converted_seed_range_list))
    result = sys.maxsize
    for converted_seed_range in converted_seed_range_list:
        result = min(result, converted_seed_range.start)

    return result

###### Unit test ######


def test_convert_seed_interval_1():
    mapping = MappingInterval(0, 4, -100)
    mapping2 = MappingInterval(5, 20, 100)
    seed_interval = SeedInterval(0, 10)
    result = convert_seed_interval(seed_interval, [[mapping, mapping2]])
    assert result[0].start == -100
    assert result[0].stop == -96
    assert result[1].start == 100
    assert result[1].stop == 105


def test_convert_seed_interval_2():
    mapping = MappingInterval(1, 4, -100)
    mapping2 = MappingInterval(6, 9, 100)
    seed_interval = SeedInterval(0, 10)
    result = convert_seed_interval(seed_interval, [[mapping, mapping2]])
    assert result[0].start == 0
    assert result[0].stop == 0
    assert result[1].start == 5
    assert result[1].stop == 5
    assert result[2].start == 10
    assert result[2].stop == 10
    assert result[3].start == -100
    assert result[3].stop == -97
    assert result[4].start == 100
    assert result[4].stop == 103

def test_convert_seed_interval_3():
    mapping = MappingInterval(77, 99, 45)
    mapping_2 = MappingInterval(45, 63, 81)
    mapping_3 = MappingInterval(64, 76, 68)
    seed_interval = SeedInterval(74, 87)
    result = convert_seed_interval(seed_interval, [[mapping, mapping_2, mapping_3]])
    print(result)
    assert result[0].start == 45
    assert result[0].stop == 55
    assert result[1].start == 78
    assert result[1].stop == 80


# test_convert_seed_interval_1()
# test_convert_seed_interval_2()
# test_convert_seed_interval_3()
# test_convert_seed_range_2()
# test_convert_seed_range_3()
# test_convert_seed_range_4()
# test_convert_seed_range_5()
# test_convert_seed_range_6()
print(calculate_lowest_location_number_2(input))
