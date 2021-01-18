def fib(n, hash_table = {}):
    if n <= 2:
        return n
    else:
        if n in hash_table:
            return hash_table[n]
        else:
            hash_table[n] = fib(n-1, hash_table) + fib(n-2, hash_table)
            return hash_table[n]

print(fib(12))
