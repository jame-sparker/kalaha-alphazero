from package.kalaha.kalaha import Kalaha
from package.tictactoe.tictactoe import TicTacToe
from package.alphazero.alphazero import AlphaZero
from package.environment import P1, P2
from package.minimax.minimax import Minimax

import argparse

EPISODES = 2001
LOG = "result.log"
TEST = True

MINIMAX_DEPTH_RANGE = 7
# test agent against minimax player
def test_agent(env, agent):
    print("-- Testing agent -- ")
    win_by_agent = [0] * MINIMAX_DEPTH_RANGE

    for depth in range(MINIMAX_DEPTH_RANGE):
        print("Opponent depth = {} ".format(depth))
        print()
        wins = 0

        minimax_agent = Minimax(depth, env)
        
        play_game(env, minimax_agent, agent, agent.evaluate, True)
        wins += env.winner() == P2
        wins += 0.5 * (env.winner() == 0)
        env.reset()
        
        play_game(env, agent, minimax_agent, agent.evaluate, True)
        wins += env.winner() == P1
        wins += 0.5 * (env.winner() == 0)
        env.reset()
        
        print("--- Won {} games against depth {} ---".format(wins, depth))
        if wins == 0:
            break

        win_by_agent[depth] = wins
    

    with open(LOG, "a") as logfile:
        logfile.write(" ".join(str(n) for n in win_by_agent) + "\n")

    print(win_by_agent)

def play_game(env, player1, player2, evaluate, verbose=False, temp=0):

    player1.set_player(P1)
    player2.set_player(P2)

    player1.init_new_game()
    player2.init_new_game()


    while not env.is_complete():
        if verbose:
            print(env)
            print("---------")
            print(evaluate(env))
            print()
        
        current_player = player1 if env.get_turn() == P1 else player2
        opponent = player2 if env.get_turn() == P1 else player1

        a = current_player.get_action(temp)
        opponent.feed_op_action(a)
        env.playout(a)
        if verbose:
            print(a)
        # return

    if verbose:
        print(env)
        print("---------")
        print(evaluate(env))
        print()

def save_agent(agent):
    pass


def run(env):
    input_size = env.get_state_size()
    hidden_size = input_size
    output_size = env.get_action_size() + 1 # each action + value

    agent = AlphaZero([input_size, hidden_size, hidden_size ,output_size], env)
    best_agent = agent.copy()
    # best_agent = AlphaZero([input_size, hidden_size ,output_size], env)
    for i in range(EPISODES): 
        if i % 50 == 0 and TEST:
            test_agent(env, agent)
        print("Episode", i + 1)
        if i % 2 == 0:
            player1 = agent
            player2 = best_agent
        else:
            player1 = best_agent
            player2 = agent

        verbose = i % 50 == 0
        # verbose = True
        temp = 1 if i % 4 == 1 or i % 4 == 2 else 0
        play_game(env, player1, player2, agent.evaluate, verbose, temp)

        winner = env.winner()
        if verbose:
            print("Winner: ", winner)
        agent.update(winner)
        agent.train()
        best_agent = agent.copy()
        
        env.reset()


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Running environment settings.')
    parser.add_argument('-env', '--environment', default="kalaha", help="Environment {\"tictactoe\", \"kalaha\"}")

    args = parser.parse_args()
    print("Environment:", args.environment.title())
    if args.environment == "kalaha":
        env = Kalaha()
    elif args.environment == "tictactoe":
        env = TicTacToe()
    else:
        raise Error("Invalid environment name")
    open(LOG, 'w').close()
    run(env)