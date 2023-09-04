# Snake Game AI using Q-Learning: A Reinforcement Learning Project  
  
This project implements a reinforcement learning algorithm, Q-Learning, to train an AI to play the classic Snake game. Built using Python, the goal of this project is to maximize the AI agent's score in the game. It serves as a simple and fun way to understand and visualize how reinforcement learning works.  
  
## Introduction  


![Alt text] ('snake.png')
  
The Snake Game AI is a fundamental reinforcement learning project using Q-Learning. The project aims to train an AI agent to play the game of Snake. The agent learns the game through trial and error, deciding whether to exploit learned strategies or explore new ones. This project is an excellent example of how AI can learn and improve over time.  
  
## Features  
  
The features of this project include:  
  
- **Exploration vs. Exploitation (Epsilon-Greedy Strategy):** The agent initially explores the environment to gain knowledge. As it learns, it increasingly relies on its knowledge to exploit learned strategies.  
  
- **Reward Tuning:** Rewards are fine-tuned to teach the agent effectively. To prevent the agent from avoiding food to survive, a larger negative reward is given for dying and a larger positive reward for eating food.  
  
- **Learning Rate and Discount Factor Tuning:** These hyperparameters control the agent's learning speed and how much it values future rewards. Tuning these parameters can optimize the performance.  
  
- **Saving and Loading the Q-table:** The agent's learned knowledge (Q-table) is saved to a file after each episode. You can load this file to resume training from where you left.  
  
- **Visualizing Learning Progress:** You can visualize the agent's performance over time using the plotted graph of rewards received each episode.  
  
## Code Structure  
  
The project comprises three main Python scripts:  
  
- `game.py`: Implements the Snake and Food classes, defining the behavior of the snake and food.  
  
- `qagent.py`: Defines the QAgent class. This class implements the Q-Learning algorithm, including the epsilon-greedy strategy, Q-table updating, and saving/loading the Q-table.  
  
- `main.py`: The main script that runs the game and the reinforcement learning algorithm. It creates instances of the Snake, Food, and QAgent classes, and then enters a loop where it updates the game state and Q-table based on the agent's action.  

- `app.py`: If you want to play yourself, This is visually more appealing ;P
  

## Installation and Usage  
  
1. Clone the repository.  
2. Run `main.py` to start the game.  
  
## Final Thoughts  
  
Training a reinforcement learning model can take time, especially for complex environments. With patience, it's fascinating to observe the agent gradually learning to play the game and achieving high scores that would be difficult for a human player.  
  
## License  
  
MIT  
  
## Acknowledgments  
  
This project is a fun experiment to explore reinforcement learning in a simple game environment.  
  
