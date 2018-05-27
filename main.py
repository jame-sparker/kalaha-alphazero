from package.kalaha.kalaha import Kalaha
from package.tictactoe.tictactoe import TicTacToe
from package.alphazero.alphazero import AlphaZero
from package.environment import P1, P2


def run():
    env = Kalaha()
    input_size = env.get_state_size()
    hidden_size = input_size
    output_size = env.get_action_size() + 1 # each action + value

    agent = AlphaZero([input_size, hidden_size ,output_size], env)
    best_agent = agent.copy()
    # best_agent = AlphaZero([input_size, hidden_size ,output_size], env)
    for i in range(1000): # 1000 game plays
        print("Epoch", i )
        if i % 2 == 0:
            player1 = agent
            player2 = best_agent
        else:
            player1 = best_agent
            player2 = agent
        player1.set_player(P1)
        player2.set_player(P2)

        player1.init_new_game()
        player2.init_new_game()


        while not env.is_complete():
            if i % 50 == 0:
                print(env)
                print("---------")
                print(player1.evaluate(env))
                print()
            
            current_player = player1 if env.get_turn() == P1 else player2
            opponent = player2 if env.get_turn() == P1 else player1

            a = current_player.get_action()
            env.playout(a)
            opponent.feed_op_action(a)
            # return

        if i % 50 == 0:
            print(env)
            print("---------")
            print(player1.evaluate(env))
            print(player2.evaluate(env))
            print()
        winner = env.winner()

        agent.update(winner)
        agent.train()
        best_agent = agent.copy()
        
        env.reset()


if __name__ == "__main__":
    # needs some config
    run()