import csv
import ast
import random
from pokemonGame.Pokemon import Pokemon, MoveProperties

pokemon_filename = 'pokemon-data.csv'

header = []
pokemon_moves = {}
pokemon_box = []
move_box = []

with open(pokemon_filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

    for row in reader:
        current_row = row
        pokemon = Pokemon(current_row[0], current_row[1], current_row[2], current_row[3], current_row[4],
                          current_row[7])

        move_props = MoveProperties(current_row[0], current_row[1], current_row[5])

        pokemon_box.append(pokemon)
        move_box.append(move_props)

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


def damage(move, attacker, defender):
    random_attack = random.uniform(0.5, 1.0)  # random
    move_power = get_move_power(move)
    attack = get_attack(attacker)
    defense = get_defense(defender)
    attacker_type = get_attack_type(attacker)
    # defender_type = None
    move_type = get_move_type(move)

    if attacker_type == move_type:
        attack_bonus = 1.5
    else:
        attack_bonus = 1

    return move_power * attack/defense * attack_bonus * random_attack


if coin_toss == 0:
    winner = player_team
    loser = 'Team Rocket'

else:
    winner = 'Rocket'
    loser = player_team

print(f'Coin toss goes to ----- Team {winner} to start the attack!')


def get_attack_type(creature):
    return pokemon.poke_type


def get_attack(creature):
    return pokemon.attack


def get_defense(creature):
    return pokemon.defense


def get_move_type(move):
    return move.move_type


def get_move_power(move):
    return move.power

print(get_attack(pokemon_box[0]))


def battle(player_current_pokemon, computer_current_pokemon):
    computer_current_pokemon = rocket_pokemon.pop(0)
    player_current_pokemon = player_pokemon.pop(0)

    while len(player_pokemon) != 0 and len(rocket_pokemon) != 0:

        gather_moves = pokemon_moves.get(computer_current_pokemon.name)
        random_attack = random.sample(gather_moves, 1)
        print(f"Team Rocket's {computer_current_pokemon.name} attacks with: {random_attack}")
        damage(random_attack, computer_current_pokemon, player_current_pokemon)
    else:


        print(player_current_pokemon.name)
        print(f'Choose the move for {player_current_pokemon.name}')
        gather_moves = pokemon_moves.get(player_current_pokemon.name)
        print(gather_moves)

    if len(rocket_pokemon) == 0 & len(player_pokemon) == 0:
        exit()


battle(player,ter_current_pokemon)
