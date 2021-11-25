from functools import reduce

def fact_gen(n):
    for m in range(1, n + 1):
        yield reduce(lambda x,y: x*y, (i for i in range(1, m+1)))

for el in fact_gen(10):
     print(el)

gen = fact_gen(10)