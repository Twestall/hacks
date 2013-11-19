import sys
from itertools import combinations
from collections import defaultdict

def do_swap(array, r, l):
    array[r], array[l] = array[l], array[r]
    return ' '.join(array)

def do_reverse(array, r, l):
    array[r:l+1] = reversed(array[r:l+1])
    return ' '.join(array)

def do_sum(array, r, l):
    return sum([int(n) for n in array[r:l+1]])

def transpose(array_dict, swap_locs, action='swap'):
    out_array = defaultdict(lambda: 0)
    for array, num in array_dict.iteritems():
        for swap in swap_locs:
            r, l = swap
            if action == 'swap':
                out_array[do_swap(array.split(' '), r, l)] += num
            elif action == 'reverse':
                out_array[do_reverse(array.split(' '), r, l)] += num
            else:
                out_array['total'] += num * do_sum(array.split(' '), r, l)
                out_array['number'] += num
    return out_array    


def reverse(array_dict, swap_locs):
    out_array = defaultdict(lambda: 0)
    
first_line = True

input_data = ['3 1 1', '1 2 3']

for line in sys.stdin:
    if first_line:
        n, a, b = line.split(' ')
        first_line = False
    else:
        array = line.strip()

dicts = {array: 1}
swap_locs = [combi for combi in combinations(range(int(n)), 2)]
for i in xrange(int(a)):
    dicts = transpose(dicts, swap_locs, action='swap')
       
for i in xrange(int(b)):
    dicts = transpose(dicts, swap_locs, action='reverse')

print float(transpose(dicts, swap_locs, action='sum')['total'])/transpose(dicts, swap_locs, action='sum')['number']
