import csv
import ast
import random
from pokemonGame.Pokemon import Pokemon, MoveProperties

pokemon_filename = 'pokemon-data.csv'
move_file = 'moves-data.csv'

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

with open(move_file) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

    for row in reader:
        current_row = row
        move_props = MoveProperties(current_row[0], current_row[1], current_row[5])
        move_box.append(move_props)
# for key in pokemon_moves:
# print(key, "moves: ", pokemon_moves[key])

# Convert keys to a list
# keys_list = list(pokemon_moves)

# for pokemon in pokemon_box:
# print(pokemon)

# print(pokemon_box[0])
# Print the keys
# print(keys_list[0])

rocket_list = random.sample(pokemon_box, 3)
player_list = random.sample(pokemon_box, 3)

computer = 'Team Rocket'  # Maybe I do not need this
all_poke_dead = 'false'

coin_toss = random.randint(0, 1)

print('Welcome to Pokemon Colosseum!\n')
player_team = input('Enter Player Name\n')

print(f"Team Rocket enters with: {', '.join(str(pokemon.name) for pokemon in rocket_list)}\n")
print(f"Team {player_team} enters with: {', '.join(str(pokemon.name) for pokemon in player_list)}\n")

print('Let the battle begin!\n')


def damage(move, attacker, defender):
    random_num = random.uniform(0.5, 1.0)  # random
    move_power = get_move_power(move)
    attack = get_attack(attacker)
    defense = get_defense(defender)
    attacker_type = get_attacker_type(attacker)
    # defender_type = None
    move_type = get_move_type()

    if attacker_type == move_type:
        attack_bonus = 1.5
    else:
        attack_bonus = 1
    minus = move_power * attack / defense * attack_bonus * random_num
    defender.hp -= minus
    return print(f"{defender}'s remaining health: {defender.hp}")


if coin_toss == 0:
    winner = player_team
    loser = 'Team Rocket'

else:
    winner = 'Rocket'
    loser = player_team

print(f'Coin toss goes to ----- Team {winner} to start the attack!')


def get_attacker_type(creature):
    return creature.poke_type


def get_attack(creature):
    return creature.attack


def get_defense(creature):
    return creature.defense


def get_move_type():
    for move in move_box:
        return move.move_type


def get_move_power(move):
    return move.power


def get_moves(creature):
    return pokemon_moves.get(creature.name)


def get_player_move(player_input):
    for player_input in move_box:
        return move_props


def battle(player_pokemons, computer_pokemons):
    player_pokemon = player_pokemons.pop(0)
    computer_pokemon = computer_pokemons.pop(0)
    while len(player_list) != 0 and len(rocket_list) != 0:
        gather_moves = pokemon_moves.get(computer_pokemon.name)
        get_moves(computer_pokemon)
        random_attack = random.sample(gather_moves, 1)
        print(f"Team Rocket's {computer_pokemon.name} attacks with: {random_attack}")
        damage(random_attack, computer_pokemon, player_pokemon)

        #  print(f"{player_pokemon.name}'s remaining health: {player_pokemon.hp}") this should be done by the damage

        if player_pokemon.hp <= 0:
            print(f"{player_pokemon.name} fainted!")
            if len(player_list) > 0:
                player_pokemon = player_list.pop(0)
                print(f"Go, {player_pokemon.name}!\n")
            else:
                print("All your Pokémon fainted. Game over.")
                break

        print("It's your turn!")
        # print(f'Choose the move for {player_pokemon.name} (1-5)')
        gather_moves = pokemon_moves.get(player_pokemon.name)
        print(gather_moves)

        player_choice = input(f'Choose the move for {player_pokemon.name}')

        # Assuming the player chooses a move somehow and assigns it to the variable chosen_move
        chosen_move = get_player_move(player_choice)

        # Perform the damage calculation for the player's move
        damage(chosen_move, player_pokemon, computer_pokemon)

        # print(f"{player_pokemon.name}'s remaining health: {player_pokemon.hp}")

        if computer_pokemon.health <= 0:
            print(f"Team Rocket's {computer_pokemon.name} fainted!")
            if len(computer_pokemon) > 0:
                computer_pokemon = computer_pokemon.pop(0)
                print(f"Team Rocket sends out {computer_pokemon.name}!\n")
            else:
                print("You defeated Team Rocket. You are the Pokémon Champion!")
                break


# def battle(player_current_pokemon, computer_current_pokemon):
#    while len(player_pokemon) != 0 and len(rocket_pokemon) != 0:

#        gather_moves = pokemon_moves.get(computer_current_pokemon.name)
#       random_attack = random.sample(gather_moves, 1)
#       print(f"Team Rocket's {computer_current_pokemon.name} attacks with: {random_attack}")
#       damage(random_attack, computer_current_pokemon, player_current_pokemon)
#   else:

#       print(player_current_pokemon.name)
#       print(f'Choose the move for {player_current_pokemon.name}')
#       gather_moves = pokemon_moves.get(player_current_pokemon.name)
#       print(gather_moves)
#
#    if len(rocket_pokemon) == 0 & len(player_pokemon) == 0:
#       exit()


#  battle(player_list, rocket_list)
newPokemon = pokemon_box[3]
random_a = random.sample(get_moves(newPokemon), 1)
newMove = move_box[0]
print(newMove.name)
print(random_a)
#  print(random_a.get_move_type())
print(pokemon_box[3])

print(get_moves(newPokemon))
print(get_attack(newPokemon))
print(get_defense(newPokemon))
print(get_attacker_type(newPokemon))
