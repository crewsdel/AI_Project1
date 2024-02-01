import csv
import ast
import random

from pokemonGame.Pokemon import Pokemon

pokemon_filename = 'pokemon-data.csv'

header = []
pokemon_moves = {}
pokemon_box = []

with open(pokemon_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

    for row in reader:
        current_row = row
        pokemon = Pokemon(current_row[0], current_row[1], current_row[2], current_row[3], current_row[4],
                          current_row[7])

        pokemon_box.append(pokemon)

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
        # print(moves)
        pokemon_moves[row[0]] = ast.literal_eval(moves)  # string to list

# for key in pokemon_moves:
# print(key, "moves: ", pokemon_moves[key])

# Convert keys to a list
# keys_list = list(pokemon_moves)

# for pokemon in pokemon_box:
# print(pokemon)

# print(pokemon_box[0])
# Print the keys
# print(keys_list[0])

rocket_pokemon = random.sample(pokemon_box, 3)
player_pokemon = random.sample(pokemon_box, 3)
computer = 'Team Rocket'


def coin_toss():
    if random.randint(0, 1) < 0.5:
        return player_team
    else:
        return computer





print('Welcome to Pokemon Colosseum!\n')
player_team = input('Enter Player Name\n')

print(f"Team Rocket enters with: {', '.join(str(pokemon.name) for pokemon in rocket_pokemon)}\n")

print(f"Team {player_team} enters with: {', '.join(str(pokemon.name) for pokemon in player_pokemon)}\n")

print('Let the battle begin!\n')

winner = coin_toss()
print(f'Coin toss goes to ----- {winner} to start the attack')
