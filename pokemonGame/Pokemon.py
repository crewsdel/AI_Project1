class Pokemon:

    def __init__(self, name, poke_type, hp, attack, defense, moves):
        self.name = name
        self.poke_type = poke_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves
        # self.move_properties = move_properties

    def __str__(self):
        return f"Name: {self.name}, Type: {self.poke_type}, HP: {self.hp}, Attack: {self.attack}"


class MoveProperties:

    def __init__(self, name, move_type, power):
        self.name = name
        self.type = move_type
        self.power = power
