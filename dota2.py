import sys

from collections import defaultdict

hero_dict = defaultdict(lambda: defaultdict(lambda: 0))

with open('trainingdata.txt') as training:
	for line in training:
		split_line = line.split(',')
		result = split_line[-1]
		team_a = split_line[:5]
		team_b = split_line[5:10]

		for hero_a in team_a:
			for hero_b in team_b:
				if result == 1:
					hero_dict[hero_a][hero_b]+=1
				else:
					hero_dict[hero_b][hero_a]+=1

for line in sys.stdin:
	split_line = line.split(',')
	if len(split_line) > 1:
		team_a = split_line[:5]
		team_b = split_line[5:10]
		a_wins = 0
		b_wins = 0

		for hero_a in team_a:
			for hero_b in team_b:
				a_wins += hero_dict[hero_a][hero_b]
				b_wins += hero_dict[hero_b][hero_a]

		if a_wins > b_wins:
			print 1
		else:
			print 2
