def can_sum(target, numbers, hash_table = {}):
    if target == 0:
        return True
    elif target < 0:
        return False
    elif target in hash_table:
        return hash_table[target]
    
    for number in numbers:
        remainder = target - number
        if (can_sum(remainder, numbers, hash_table)):
            hash_table[target] = True
            return True
    hash_table[target] = False
    return False

print(can_sum(2000, [7,14,54,76,12]))

