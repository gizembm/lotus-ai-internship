from game import SnakeGameAI
from agent import Agent
import time

def play():
    agent = Agent()
    agent.load_model()
    agent.train_mode = False
    game = SnakeGameAI()

    while True:
        state = agent.get_state(game)
        final_move = agent.act(state)
        reward, done, score = game.play_step(final_move)

        time.sleep(0.05)  # izlenebilir hız

        if done:
            print("Skor:", score)
            game.reset()

if __name__ == "__main__":
    play()
