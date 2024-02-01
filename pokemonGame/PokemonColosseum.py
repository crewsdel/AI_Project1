import csv
import ast

pokemon_filename = 'pokemon-data.csv'

header = []
pokemon_moves = {}

with open(pokemon_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

    for row in reader:
        moves = ''
        end_of_moves = False
        for s in row:
            if s[0] == '[':
                end_of_moves = True
                moves = s
            elif end_of_moves:
                moves += ',' + s
                if s[-1] == ']':
                    end_of_moves = False
        #print(moves)
        pokemon_moves[row[0]] = ast.literal_eval(moves)  # string to list

for key in pokemon_moves:
    print(key, "moves: ", pokemon_moves[key])

print('Welcome to Pokemon Colosseum!\n')
player_team = input('Enter Player Name\n')
print('Team Rocket enters with BLANK BLANK BLANK\n')
print('Team' + player_team + 'enters with BLANK BLANK\n')

print('Let the battle begin!\n')
