from part2 import check_safety

bad_1 = [83, 82, 86, 87, 86]
good_1 = [48,46,47,49,51,54,56]

assert(check_safety(bad_1,0)==False)
assert(check_safety(good_1,0)==True)