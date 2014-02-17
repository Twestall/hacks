import sys
from collections import defaultdict

def load_training_data(training_file):
    hero_dict = defaultdict(lambda: defaultdict(lambda: 0))

    with open('trainingdata.txt') as training:
        for line in training:
            split_line = line.split(',')
            result = split_line[-1]
            team_a = split_line[:5]
            team_b = split_line[5:10]

            if result == 1:
                for hero in team_a:
                    hero_dict[hero]['wins'] += 1
                for hero in team_b:
                    hero_dict[hero]['losers'] += 1
            
            else:
                for hero in team_b:
                    hero_dict[hero]['wins'] += 1
                for hero in team_a:
                    hero_dict[hero]['losers'] += 1

    return hero_dict

def predict_result(heros_playing, hero_dict):
    team_a = heros_playing[:5]
    team_b = heros_playing[5:10]
    
    a_wins = 0
    a_loses = 0
        
    for hero in team_a:
        a_wins += hero_dict[hero]['wins']
        a_loses += hero_dict[hero]['loses']
    
    a_ratio = float(a_wins)/(a_wins + a_loses)

    b_wins = 0
    b_loses = 0
        
    for hero in team_b:
        b_wins += hero_dict[hero]['wins']
        b_loses += hero_dict[hero]['loses']
    
    b_ratio = float(b_wins)/(a_wins + b_loses)            
        
    if a_ratio >= b_ratio:
        return 1
    
    else:
        return 2

if __name__ == '__main__':
    hero_dict = load_training_data('trainingdata.txt')

    for line in sys.stdin:
        split_line = line.strip().split(',')
        if len(split_line) > 1:

            result = predict_result(split_line, hero_dict)
            print result
