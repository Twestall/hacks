# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

battery_life = defaultdict(lambda: [])

with open('trainingdata.txt') as train:
    for line in train:
        charge, life = tuple(line.strip().split(','))
        battery_life[float(charge)].append(float(life))
        
avgerage_life = {}

average_life = sorted([(charge, sum(life)/len(life)) for charge, life in battery_life.iteritems()])
        
import sys
data = float(sys.stdin.readline())

lower_charge = 0
lower_life = 0

for i, stats in enumerate(average_life):
    charge, life = stats
    if data <= charge:
        if data == charge:
            print life
        else:
            upper_charge = charge
            upper_life = life
            charge_diff = upper_charge - lower_charge
            percent_place = (data - lower_charge)/charge_diff
            
            print lower_life + (upper_life - lower_life) * percent_place
            break
            
    else:
        lower_charge = charge
        lower_life = life 
