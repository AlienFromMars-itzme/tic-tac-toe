"""
Example of human vs AI game.
"""

from tictactoe import TicTacToe, HumanPlayer, SmartAI, ConsoleInterface

def main():
    # Create a new game
    game = TicTacToe()
    interface = ConsoleInterface(game)
    
    # Create players
    human = HumanPlayer('X', "Human Player")
    ai = SmartAI('O', "Smart AI", difficulty="hard")
    
    print("🤖 Human vs AI Tic-Tac-Toe!")
    print("You are X, AI is O")
    
    # Play the game
    interface.play_game(human, ai)

if __name__ == "__main__":
    main()