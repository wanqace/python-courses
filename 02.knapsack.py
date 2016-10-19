#!/usr/bin/env python

def knapsack(capacity, items):
    # create dict {density: items_index]
    index = 0
    values = dict()
    for i in items:
        values[ float(i[1]) / i[0] ] = index
        index += 1

    # create zero list
    result = [0 for i in items]
    free = capacity
    # try to put every item sorted by density
    for val in sorted(values, reverse=True):
        index = values[val]
        while free >= items[index][0]:
            result[index] += 1
            free -= items[index][0]
    return result


# [size, value]
items = [ [10, 20], [5, 9], [20, 45], [2, 1] ]
capacity = 54
print capacity, items
print knapsack(capacity, items)

