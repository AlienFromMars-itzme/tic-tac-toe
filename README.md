# Tic-Tac-Toe Library

A comprehensive Python library for creating tic-tac-toe games with support for human players, AI opponents, and customizable interfaces.

## Features

- 🎮 Complete tic-tac-toe game logic
- 🤖 Multiple AI difficulty levels (Random, Smart)
- 👥 Human player support
- 📊 Game statistics tracking
- 🖥️ Console interface
- 🔧 Extensible architecture for custom players and interfaces
- 📦 Easy to use and integrate

## Installation

```bash
pip install -e .
```

## Quick Start

### Basic Human vs Human Game

```python
from tictactoe import TicTacToe, HumanPlayer, ConsoleInterface

# Create game and interface
game = TicTacToe()
interface = ConsoleInterface(game)

# Create players
player1 = HumanPlayer('X', "Alice")
player2 = HumanPlayer('O', "Bob")

# Play the game
interface.play_game(player1, player2)
```

### Human vs AI Game

```python
from tictactoe import TicTacToe, HumanPlayer, SmartAI, ConsoleInterface

game = TicTacToe()
interface = ConsoleInterface(game)

human = HumanPlayer('X', "Human")
ai = SmartAI('O', "AI Assistant", difficulty="hard")

interface.play_game(human, ai)
```

### Custom Game Logic

```python
from tictactoe import TicTacToe

# Create and control game manually
game = TicTacToe()

# Make moves
game.make_move(4)  # Center position
game.make_move(0)  # Top-left corner

# Check game state
print(f"Current player: {game.current_player}")
print(f"Available moves: {game.get_available_moves()}")
print(f"Game over: {game.is_game_over()}")

# Display board
print(game)
```

## Classes Overview

### Core Classes

- **`TicTacToe`**: Main game logic and state management
- **`Player`**: Abstract base class for all player types
- **`HumanPlayer`**: Interactive human player
- **`RandomAI`**: AI that makes random moves
- **`SmartAI`**: AI using minimax algorithm
- **`ConsoleInterface`**: Terminal-based game interface
- **`GameStats`**: Statistics tracking across multiple games

### Game States

- `GameState.ONGOING`: Game in progress
- `GameState.X_WINS`: X player won
- `GameState.O_WINS`: O player won  
- `GameState.DRAW`: Game ended in draw

## Examples

See the `examples/` directory for more detailed usage examples:

- `basic_game.py`: Simple human vs human game
- `human_vs_ai.py`: Human vs AI with different difficulty levels
- `tournament.py`: Multiple games with statistics tracking

## API Reference

### TicTacToe Class

```python
class TicTacToe:
    def __init__(self)
    def reset(self)
    def make_move(position: int) -> bool
    def is_valid_move(position: int) -> bool
    def get_available_moves() -> List[int]
    def is_game_over() -> bool
    def get_board_copy() -> List[str]
```

### Player Classes

```python
class Player(ABC):
    def __init__(symbol: str, name: str = "")
    def get_move(game: TicTacToe) -> int  # Abstract method

class HumanPlayer(Player):
    # Gets input from user via console

class RandomAI(Player):
    # Makes random valid moves

class SmartAI(Player):
    def __init__(symbol: str, name: str = "", difficulty: str = "hard")
    # Uses minimax algorithm, difficulty: "easy" or "hard"
```

## Creating Custom Players

Extend the `Player` class to create custom player implementations:

```python
from tictactoe import Player, TicTacToe

class MyCustomAI(Player):
    def get_move(self, game: TicTacToe) -> int:
        # Your custom logic here
        available_moves = game.get_available_moves()
        # Return chosen position (0-8)
        return available_moves[0]
```

## Statistics Tracking

```python
from tictactoe import GameStats

stats = GameStats()

# After each game:
stats.record_game(game.game_state, game.moves_count)

# View statistics:
stats.print_stats()
print(stats.get_stats())  # Returns dict with detailed stats
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Author

Created by AlienFromMars-itzme