# qagent.py  
import numpy as np  
from game import Snake, Food  
  
# qagent.py  
import numpy as np  
from game import Snake, Food  

UP = (0,-1)  
DOWN = (0,1)  
LEFT = (-1,0)  
RIGHT = (1,0)   
SCREEN_WIDTH = 480  
SCREEN_HEIGHT = 480  
  
GRIDSIZE = 20  
GRID_WIDTH = SCREEN_WIDTH // GRIDSIZE  
GRID_HEIGHT = SCREEN_HEIGHT // GRIDSIZE  

class QAgent:  
    def __init__(self):  
        self.q_table = np.zeros((GRID_WIDTH, GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT, 4, 4))
        self.learning_rate = 0.5
        self.discount_factor = 0.95  
        self.epsilon = 1.0  # exploration rate  
        self.epsilon_decay = 0.999  # the rate at which exploration rate decreases  
        self.epsilon_min = 0.01  # the minimum exploration rate  
        self.q_table_file = "q_table.npy"
  
    def get_action(self, state):  
        if np.random.rand() <= self.epsilon:  
            # Explore: select a random action  
            return np.random.choice([0, 1, 2, 3])  
        else:  
            # Exploit: select the action with max Q-value (expected future reward)  
            return np.argmax(self.q_table[state])  
  
    def get_state(self, snake, food):  
        head_x, head_y = snake.get_head_position()  
        head_x, head_y = head_x // GRIDSIZE, head_y // GRIDSIZE  
  
        food_x, food_y = food.position  
        food_x, food_y = food_x // GRIDSIZE, food_y // GRIDSIZE  
  
        # Direction of snake  
        if snake.direction == UP:  
            direction = 0  
        elif snake.direction == DOWN:  
            direction = 1  
        elif snake.direction == LEFT:  
            direction = 2  
        elif snake.direction == RIGHT:  
            direction = 3  
  
        return (head_x, head_y, food_x, food_y, direction) 


    def decay_epsilon(self):  
        # Decrease epsilon  
        if self.epsilon > self.epsilon_min:  
            self.epsilon *= self.epsilon_decay  
  
    def update_q_table(self, old_state, action, reward, new_state, done):  
        if done:  
            self.q_table[old_state + (action,)] = reward  
        else:  
            max_future_q = self.get_max_future_q_value(new_state)  
            current_q = self.q_table[old_state + (action,)]  
            new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (reward + self.discount_factor * max_future_q)  
            self.q_table[old_state + (action,)] = new_q
  
    def get_max_future_q_value(self, state):  
        # Get the maximum future Q-value for a given state  
        return np.max(self.q_table[state])  

    def save_q_table(self):  
        np.save(self.q_table_file, self.q_table)  
  
    def load_q_table(self):  
        self.q_table = np.load(self.q_table_file, allow_pickle=True)  
