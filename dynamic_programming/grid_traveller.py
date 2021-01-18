def grid_trav(n,m,hash_table={}):
    key = str(n) + ',' + str(m)
    if n == 0 or m == 0:
        return 0
    elif n == 1 or m == 1:
        return 1
    else:
        if key in hash_table:
            return hash_table[key]
        else:
            hash_table[key] = grid_trav(n,m-1,hash_table) + grid_trav(n-1,m,hash_table)
            return hash_table[key]

print(grid_trav(18,18))