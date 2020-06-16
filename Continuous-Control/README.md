
**Introduction:**

For this project, [Reacher](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#reacher) environment was used.

![Alt Text](https://github.com/manoj-aryal/Deep-RL-Nanodegree/blob/master/Continuous-Control/screenshot.gif)

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of our agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

**Distributed Training:**

For this project, Unity environment containing 20 identical agents were provided.

And algorithms like PPO, A3C, and D4PG that use multiple (non-interacting, parallel) copies of the same agent to distribute the task of gathering experience were explored.

**Solving the environment:**

The agents must get an average score of +30 (over 100 consecutive episodes, and over all agents). Specifically,

After each episode, rewards that each agent received (without discounting) were added, to get a score for each agent. This yielded 20 (potentially different) scores. Then we can take the average of these 20 scores.
This yields an average score for each episode (where the average is over all 20 agents).
The environment is considered solved, when the average (over 100 episodes) of those average scores is at least +30.

**Getting Started:**

Download the environment from one of the links below. You need only select the environment that matches your operating system:

**Twenty (20) Agents:**

- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)

(For Windows users) Check out this [link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(For AWS) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux_NoVis.zip) (version 1) or [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux_NoVis.zip) (version 2) to obtain the "headless" version of the environment. You will not be able to watch the agent without enabling a virtual screen, but you will be able to train the agent. (To watch the agent, you should follow the instructions to [enable a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the Linux operating system above.)

Place the file in the DRLND GitHub repository, in the p2_continuous-control/ folder, and unzip (or decompress) the file.

**Dependencies:**

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

- Linux or Mac:
conda create --name drlnd python=3.6
source activate drlnd

- Windows:
conda create --name drlnd python=3.6 
activate drlnd

2. Follow the instructions [in this](https://github.com/openai/gym) repository to perform a minimal install of OpenAI gym.

- Next, install the classic control environment group by following the instructions [here](https://github.com/openai/gym#classic-control).
- Then, install the box2d environment group by following the instructions [here](https://github.com/openai/gym#box2d).

3. Clone the repository (if you haven't already!), and navigate to the python/ folder. Then, install several dependencies.

git clone https://github.com/udacity/deep-reinforcement-learning.git
cd deep-reinforcement-learning/python
pip install .

4. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the drlnd environment.

python -m ipykernel install --user --name drlnd --display-name "drlnd"

5. Before running code in a notebook, change the kernel to match the drlnd environment by using the drop-down Kernel menu.


**Instructions:**

Follow the instructions in Continuous_Control.ipynb to get started with training your own agent!
