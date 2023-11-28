# Game Scene Render

## Overview
This application simulates a game environment where characters can be placed, moved, and interact with buildings in different areas. It allows for creating various types of characters and buildings, each with specific attributes.

## Design Patterns Used

### Factory Method Pattern
- **Usage**: Applied in the `BuildingFactory` class.
- **Purpose**: To create objects (buildings) without specifying the exact class of object that will be created. This pattern is used to generate different types of buildings based on the area type (European, Asian, African).

### Class Inheritance
- **Usage**: Seen in the `ConcreteHouse`, `BambooHouse`, and `WailCaneHouse` classes, all inheriting from the `Building` base class.
- **Purpose**: To create specialized versions of a building with shared characteristics. This allows for easy expansion and addition of new building types.

### Encapsulation
- **Usage**: Applied in the `Character` and `Area` classes.
- **Purpose**: To bundle the data (attributes like position, age, abilities) and methods applicable to a specific entity, ensuring that the internal representation of the object is hidden from the outside.

## Functionalities

- **Area Creation**: Users can create an area with a specific name.
- **Building Creation**: Users can create buildings of specific types, sizes, and positions, depending on the area type.
- **Character Creation**: Users can create characters with specified attributes like type, age, position, size, and abilities.
- **Character Movement**: Users can move characters around the area, with collision detection to prevent moving into a building's space.

## How to Run

1. Start the application.
2. Follow the on-screen prompts to create an area, buildings, and a character.
3. Use the movement commands to move the character within the area.

Note: Ensure to input values as prompted, following the required formats for positions (x, y) and sizes (width, length).
