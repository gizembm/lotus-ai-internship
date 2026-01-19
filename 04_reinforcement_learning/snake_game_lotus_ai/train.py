from game import SnakeGameAI
from agent import Agent

MAX_GAMES = 700

def train():
    agent = Agent()
    game = SnakeGameAI()
    record = 0

    while agent.n_games < MAX_GAMES:
        state_old = agent.get_state(game)
        final_move = agent.act(state_old)
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.save_model()
                print("Yeni en iyi model kaydedildi!")

            print(f"Oyun: {agent.n_games}/{MAX_GAMES}, Skor: {score}, Rekor: {record}")

    print("✅ Eğitim tamamlandı (500 oyun oynandı).")

if __name__ == "__main__":
    train()
