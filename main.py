class Building:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def __str__(self):
        return f"{self.__class__.__name__} (Position: {self.position}, Size: {self.size})"

class ConcreteHouse(Building):
    pass

class BambooHouse(Building):
    pass

class WailCaneHouse(Building):
    pass

class BuildingFactory:
    def create_building(self, area_type, position, size):
        if area_type == "European":
            return ConcreteHouse(position, size)
        elif area_type == "Asian":
            return BambooHouse(position, size)
        elif area_type == "African":
            return WailCaneHouse(position, size)
        else:
            raise ValueError(f"Unknown area type: {area_type}")

class Area:
    def __init__(self, name):
        self.name = name
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

    def is_position_clear(self, position):
        for building in self.buildings:
            if building.position == position:
                return False
        return True

    def __str__(self):
        buildings_info = "\n".join(str(building) for building in self.buildings)
        return f"Area: {self.name}\nBuildings:\n{buildings_info}"

class Character:
    def __init__(self, character_type, age, position, size, abilities):
        self.character_type = character_type
        self.age = age
        self.position = position
        self.size = size
        self.abilities = abilities

    def move(self, direction, steps=3):
        dx, dy = 0, 0
        if direction == "up":
            dy = -steps
        elif direction == "down":
            dy = steps
        elif direction == "left":
            dx = -steps
        elif direction == "right":
            dx = steps
        return (self.position[0] + dx, self.position[1] + dy)

    def __str__(self):
        return f"{self.character_type} (Age: {self.age}, Position: {self.position}, Size: {self.size}, Abilities: {self.abilities})"

def move_character_if_possible(area, character, direction):
    new_position = character.move(direction)
    if area.is_position_clear(new_position):
        character.position = new_position
        return f"{character.character_type} moved to {new_position}"
    else:
        return f"Move blocked: Cannot move {direction}. Building at {new_position}"

area_name = input("Enter the name of the land: ")
area = Area(area_name)

# Creating a building based on user input
factory = BuildingFactory()
building_type = input("Enter building type (European/Asian/African): ")
building_position = tuple(map(int, input("Enter building position (x, y): ").split(',')))
building_size = tuple(map(int, input("Enter building size (width, length): ").split(',')))
building = factory.create_building(building_type, building_position, building_size)
area.add_building(building)

# Creating a character based on user input
character_type = input("Enter character type: ")
character_age = int(input("Enter character age: "))
character_position = tuple(map(int, input("Enter character position (x, y): ").split(',')))
character_size = input("Enter character size: ")
character_abilities = input("Enter character abilities (comma-separated): ").split(',')
character = Character(character_type, character_age, character_position, character_size, character_abilities)

# Interactive character movement
while True:
    move_direction = input("Enter move direction (up/down/left/right) or 'quit' to exit: ")
    if move_direction.lower() == 'quit':
        break
    move_result = move_character_if_possible(area, character, move_direction)
    print(move_result)

# Print the final state of the area and character
print(area)
print(character)

# Attempting to move the character in various directions
move_results = [
    move_character_if_possible(area, character, "up"),
    move_character_if_possible(area, character, "down"),
    move_character_if_possible(area, character, "left"),
    move_character_if_possible(area, character, "right")
]

# Print the movement results and the current state of the area and character
for result in move_results:
    print(result)

print(area)
print(character)
