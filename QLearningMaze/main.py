from environment import Maze
from brain import QLearningTable

def update():
    for episode in range(100):
        # current state
        S = env.reset()

        while True:
            # fresh environment
            env.render()

            A = RL.choose_action(str(S))

            S_, R, done = env.step(A)

            RL.learn(str(S), A, R, str(S_))

            # update
            S = S_

            if done:
                break

    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()