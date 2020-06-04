# Project 1: Navigation

**Introduction**

For this project, an agent was trained to navigate (and collect bananas!) in a large, square world.

![Alt Text](https://github.com/manoj-aryal/Deep-Reinforcement-Learning-Nanodegree/blob/master/Navigation-DeepQN/project1.gif)

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of an agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction. Given this information, the agent learned how to best select actions. Four discrete actions are available, corresponding to:

- 0 - move forward.
- 1 - move backward.
- 2 - turn left.
- 3 - turn right.

The task is episodic, and in order to solve the environment, agent must get an average score of +13 over 100 consecutive episodes. And it did!

Getting Started
Download the environment from one of the links below. You need only select the environment that matches your operating system:

Linux: click here
Mac OSX: click here
Windows (32-bit): click here
Windows (64-bit): click here
(For Windows users) Check out this link if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use this link to obtain the environment.

Place the file in this folder, unzip (or decompress) the file and then write the correct path in the argument for creating the environment under the notebook Navigation_solution.ipynb:

env = env = UnityEnvironment(file_name="Banana.app")
Description
dqn_agent.py: code for the agent used in the environment
model.py: code containing the Q-Network used as the function approximator by the agent
dqn.pth: saved model weights for the original DQN model
ddqn.pth: saved model weights for the Double DQN model
ddqn.pth: saved model weights for the Dueling Double DQN model
Navigation_exploration.ipynb: explore the unity environment
Navigation_solution.ipynb: notebook containing the solution
Navigation_Pixels.ipynb: notebook containing the code for the pixel-action problem (see below)
Instructions
Follow the instructions in Navigation_solution.ipynb to get started with training your own agent! To watch a trained smart agent, follow the instructions below:

DQN: If you want to run the original DQN algorithm, use the checkpoint dqn.pth for loading the trained model. Also, choose the parameter qnetwork as QNetwork while defining the agent and the parameter update_type as dqn.
Double DQN: If you want to run the Double DQN algorithm, use the checkpoint ddqn.pth for loading the trained model. Also, choose the parameter qnetwork as QNetwork while defining the agent and the parameter update_type as double_dqn.
Dueling Double DQN: If you want to run the Dueling Double DQN algorithm, use the checkpoint dddqn.pth for loading the trained model. Also, choose the parameter qnetwork as DuelingQNetwork while defining the agent and the parameter update_type as double_dqn.
Enhancements
Several enhancements to the original DQN algorithm have also been incorporated:

Double DQN [Paper] [Code]
Prioritized Experience Replay [Paper] [Code] (WIP)
Dueling DQN [Paper] [Code]
Results
Plot showing the score per episode over all the episodes. The environment was solved in 377 episodes (currently).

Double DQN	DQN	Dueling DQN
double-dqn-scores	dqn-scores	dueling-double-dqn-scores
Challenge: Learning from Pixels
In the project, your agent learned from information such as its velocity, along with ray-based perception of objects around its forward direction. A more challenging task would be to learn directly from pixels!

To solve this harder task, you'll need to download a new Unity environment. This environment is almost identical to the project environment, where the only difference is that the state is an 84 x 84 RGB image, corresponding to the agent's first-person view. (Note: Udacity students should not submit a project with this new environment.)

You need only select the environment that matches your operating system:

Linux: click here
Mac OSX: click here
Windows (32-bit): click here
Windows (64-bit): click here
Then, place the file in this folder, and unzip (or decompress) the file. Next, open Navigation_Pixels.ipynb and follow the instructions to learn how to use the Python API to control the agent.

(For AWS) If you'd like to train the agent on AWS, you must follow the instructions to set up X Server, and then download the environment for the Linux operating system above.

Dependencies
Use the requirements.txt file (in the main folder) to install the required dependencies via pip.

pip install -r requirements.txt
