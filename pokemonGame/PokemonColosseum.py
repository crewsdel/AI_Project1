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
    for move_props in move_box:
        if str(move) == move_props.name:
            move = move_props
            break
    random_num = random.uniform(0.5, 1.0)  # random
    move_power = get_move_power(move)
    int(move_power)
    attack = get_attack(attacker)
    int(attack)
    defense = get_defense(defender)
    int(defense)
    attacker_type = get_attacker_type(attacker)
    # defender_type = None
    move_type = move.move_type

    if attacker_type == move_type:
        attack_bonus = 1.5
    else:
        attack_bonus = 1

    minus = move_power * attack / defense * attack_bonus * random_num
    return int(minus)


def get_attacker_type(creature):
    return creature.poke_type


def get_attack(creature):
    return creature.attack


def get_defense(creature):
    return creature.defense


def get_hp(creature):
    return creature.hp


def get_move_power(move):
    return move.power


def get_moves(creature):
    return pokemon_moves.get(creature.name)


def get_player_move(player_input):
    for move_props in move_box:
        if player_input == move_props.name:
            player_input = move_props
        return player_input


def battle():
    coin_toss_winner = random.choice(["Player", "Computer"])

    if coin_toss_winner == "Player":
        print("You won the coin toss! You go first!\n")
        player_pokemon = player_list.pop(0)
        computer_pokemon = rocket_list.pop(0)
        while (player_pokemon.hp > 0 and len(player_list) != 0) or (computer_pokemon.hp > 0 and len(rocket_list) != 0):

            gather_moves = pokemon_moves.get(player_pokemon.name)
            print(gather_moves)

            player_choice = input(f"Choose the move for {player_pokemon.name} ex: ['Dig'] ")
            if player_choice.isnumeric():
                print("Invalid input! strings only!")
                player_choice = input(f"Choose the move for {player_pokemon.name} ex: ['Dig'] ")

            chosen_move = get_player_move(player_choice)

            computer_pokemon.hp = computer_pokemon.hp - damage(chosen_move, player_pokemon, computer_pokemon)
            print(f"{computer_pokemon.name}'s remaining health: {computer_pokemon.hp}")

            if computer_pokemon.hp <= 0:
                print(f"Team Rocket's {computer_pokemon.name} fainted!")
                if len(rocket_list) > 0:
                    computer_pokemon = rocket_list.pop(0)
                    print(f"Team Rocket sends out {computer_pokemon.name}!\n")
                else:
                    print("You defeated Team Rocket. You are the Pokémon Champion!")
                    break

            print("It's Team Rocket's turn!\n")
            gather_moves = pokemon_moves.get(computer_pokemon.name)
            get_moves(computer_pokemon)
            random_attack = random.sample(gather_moves, 1)
            print(f"Team Rocket's {computer_pokemon.name} attacks with: {random_attack}")
            int(player_pokemon.hp)
            player_pokemon.hp = int(player_pokemon.hp) - damage(random_attack, computer_pokemon, player_pokemon)

            print(f"{player_pokemon.name}'s remaining health: {player_pokemon.hp}\n")

            if player_pokemon.hp <= 0:
                print(f"{player_pokemon.name} fainted!")
                if len(player_list) > 0:
                    player_pokemon = player_list.pop(0)
                    print(f"Go, {player_pokemon.name}!\n")
                else:
                    print("All your Pokémon fainted. Game over.")
                    break

    else:
        print(f"Team Rocket won the coin toss, they go first\n")
        player_pokemon = player_list.pop(0)
        computer_pokemon = rocket_list.pop(0)

        while (player_pokemon.hp > 0 and len(player_list) != 0) or (computer_pokemon.hp > 0 and len(rocket_list) != 0):
            gather_moves = pokemon_moves.get(computer_pokemon.name)
            get_moves(computer_pokemon)
            random_attack = random.sample(gather_moves, 1)
            print(f"Team Rocket's {computer_pokemon.name} attacks with: {random_attack}")
            int(player_pokemon.hp)
            player_pokemon.hp = int(player_pokemon.hp) - damage(random_attack, computer_pokemon, player_pokemon)

            print(f"{player_pokemon.name}'s remaining health: {player_pokemon.hp}\n")

            if player_pokemon.hp <= 0:
                print(f"{player_pokemon.name} fainted!")
                if len(player_list) > 0:
                    player_pokemon = player_list.pop(0)
                    print(f"Go, {player_pokemon.name}!\n")
                else:
                    print("All your Pokémon fainted. Game over.")
                    break

            print("It's your turn!")
            gather_moves = pokemon_moves.get(player_pokemon.name)
            print(gather_moves)

            player_choice = input(f"Choose the move for {player_pokemon.name} ex: ['Dig'] ")
            if player_choice.isnumeric():
                print("Invalid input! strings only!")
                player_choice = input(f"Choose the move for {player_pokemon.name} ex: ['Dig'] ")

            chosen_move = get_player_move(player_choice)

            computer_pokemon.hp = computer_pokemon.hp - damage(chosen_move, player_pokemon, computer_pokemon)
            print(f"{computer_pokemon.name}'s remaining health: {computer_pokemon.hp}")

            if computer_pokemon.hp <= 0:
                print(f"Team Rocket's {computer_pokemon.name} fainted!")
                if len(rocket_list) > 0:
                    computer_pokemon = rocket_list.pop(0)
                    print(f"Team Rocket sends out {computer_pokemon.name}!\n")
                else:
                    print("You defeated Team Rocket. You are the Pokémon Champion!")
                    break


battle()
