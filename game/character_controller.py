
class CharacterController:
    def __init__(self, space_ship):
        self.space_ship = space_ship

    def update_character(self):
        self.space_ship.update()
