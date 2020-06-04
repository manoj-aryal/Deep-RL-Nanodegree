import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.epsilon = 1.0
        self.alpha = 0.018
        self.num_episodes = 1
        self.gamma = 1
        
    def epsilon_greedy_probs(self, state):
        policy_s = np.ones(self.nA) * self.epsilon / self.nA
        policy_s[np.argmax(self.Q[state])] = 1 - self.epsilon + (self.epsilon / self.nA)
        return policy_s

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        
        """
        policy_s = self.epsilon_greedy_probs(state)
        return np.random.choice(self.nA, p = policy_s)

    
    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        
        if not done:
            self.Q[state][action] = self.Q[state][action] + (self.alpha * (reward + (self.gamma 
                                                                                     * np.max(self.Q[next_state])) - self.Q[state][action]))
            
        if done:
            self.Q[state][action] = self.Q[state][action] + (self.alpha * (reward - self.Q[state][action]))
            self.num_episodes += 1
            self.epsilon = 1.0 / self.num_episodes
            
            