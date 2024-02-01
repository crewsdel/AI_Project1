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

computer = 'Team Rocket'  # Maybe I do not need this
all_poke_dead = 'false'

coin_toss = random.randint(0, 1)

print('Welcome to Pokemon Colosseum!\n')
player_team = input('Enter Player Name\n')

print(f"Team Rocket enters with: {', '.join(str(pokemon.name) for pokemon in rocket_pokemon)}\n")
print(f"Team {player_team} enters with: {', '.join(str(pokemon.name) for pokemon in player_pokemon)}\n")

print('Let the battle begin!\n')


# winner = 'Team Rocket'  # coin_toss()
def is_alive(self):
    return self.health > 0


if coin_toss == 0:
    winner = player_team
    loser = 'Team Rocket'

else:
    winner = 'Rocket'
    loser = player_team

print(f'Coin toss goes to ----- Team {winner} to start the attack!')

computer_current_pokemon = rocket_pokemon.pop(0)
player_current_pokemon = player_pokemon.pop(0)


def battle(player_current_pokemon, computer_current_pokemon):
    computer_current_pokemon = rocket_pokemon.pop(0)
    player_current_pokemon = player_pokemon.pop(0)
    while len(player_pokemon) != 0 and len(rocket_pokemon) != 0:

        gather_moves = pokemon_moves.get(computer_current_pokemon.name)
        random_attack = random.sample(gather_moves, 1)
        print(f"Team Rocket's {computer_current_pokemon.name} attacks with: {random_attack}")

    else:


        print(player_current_pokemon.name)
        print(f'Choose the move for {player_current_pokemon.name}')
        gather_moves = pokemon_moves.get(player_current_pokemon.name)
        print(gather_moves)

    if len(rocket_pokemon) == 0 & len(player_pokemon) == 0:
        exit()


battle(player_current_pokemon, computer_current_pokemon)
