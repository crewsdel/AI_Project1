class Pokemon:
    pass
    def __init__(self, name, poke_type, hp, attack, defense, moves, move_properties):
        self.name = name
        self.poke_type = poke_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves
        self.move_properties = move_properties

    def __str__(self):
        return (f"Name: {self.name}, Type: {self.poke_type}, HP: {self.hp}, Attack: {self.attack},"
                f" Defense: {self.defense}, Moves: {self.moves}, MoveProperties: {self.move_properties}")

    Obj = Pokemon("Pika", "electric", 100, 100, 100, ['thunder', 'thunder', 'thunder', 'lightning'], ['fire, angel'])
    print(Obj)

