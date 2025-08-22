"""
Example of running multiple games and tracking statistics.
"""

from tictactoe import TicTacToe, RandomAI, SmartAI, ConsoleInterface, GameStats

def main():
    stats = GameStats()
    
    print("🏆 AI Tournament: Random AI vs Smart AI")
    print("Running 10 games...")
    
    for i in range(10):
        # Create new game for each round
        game = TicTacToe()
        interface = ConsoleInterface(game)
        
        # Create AI players
        random_ai = RandomAI('X', f"Random AI")
        smart_ai = SmartAI('O', f"Smart AI")
        
        print(f"\n--- Game {i+1} ---")
        
        # Play without showing board (silent mode)
        players = {'X': random_ai, 'O': smart_ai}
        
        while not game.is_game_over():
            current_player = players[game.current_player]
            move = current_player.get_move(game)
            game.make_move(move)
        
        # Record results
        stats.record_game(game.game_state, game.moves_count)
        
        # Show result
        if game.game_state.value.endswith('wins'):
            winner = "Random AI" if "x" in game.game_state.value else "Smart AI"
            print(f"Winner: {winner}")
        else:
            print("Draw!")
    
    # Show final statistics
    stats.print_stats()

if __name__ == "__main__":
    main()