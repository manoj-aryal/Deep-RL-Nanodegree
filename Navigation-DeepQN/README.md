# Project 1: Navigation

**Introduction**

For this project, an agent was trained to navigate (and collect bananas!) in a large, square world.

![Alt Text](https://github.com/manoj-aryal/Deep-Reinforcement-Learning-Nanodegree/blob/master/Navigation-DeepQN/project1.gif)

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of an agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction. Given this information, the agent learned how to best select actions. Four discrete actions are available, corresponding to:

0 - move forward.
1 - move backward.
2 - turn left.
3 - turn right.
The task is episodic, and in order to solve the environment, agent must get an average score of +13 over 100 consecutive episodes. And it did!
