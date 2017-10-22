import numpy as np
import pandas as pd

class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions
        self.alpha = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions)

    def choose_action(self, S):
        self.check_state_exist(S)

        if np.random.uniform() < self.epsilon:
            # choose max action
            state_action = self.q_table.ix[S, :]
            print("State Action: ", state_action)
            state_action = state_action.reindex(np.random.permutation(state_action.index))  # some actions have value
            print("State Action B: ", state_action)
            A = state_action.argmax()
            print("Argmax: ", A)
        else:
            # choose random action
            A = np.random.choice(self.actions)

        return A

    def learn(self, S, A, R, S_):
        self.check_state_exist(S_)

        q_predict = self.q_table.ix[S, A]
        if S_ != 'terminal':
            q_target = R + self.gamma * self.q_table.ix[S_, :].max()
        else:
            q_target = R

        self.q_table.ix[S, A] += self.alpha * (q_target - q_predict)

    def check_state_exist(self, S):
        if S not in self.q_table.index:
            # append new state to table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),  # add columns
                    index=self.q_table.columns,
                    name=S,
                )
            )
