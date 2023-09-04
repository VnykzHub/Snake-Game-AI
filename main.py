# main.py  
import pygame  
import os
from game import *
from game import Snake, Food  
from qagent import QAgent  
import matplotlib.pyplot as plt  

NUM_EPISODES = 5000 

def main():  
    pygame.init()  
    clock = pygame.time.Clock()  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
  
    snake = Snake()  
    food = Food()  
    agent = QAgent()  
    if os.path.isfile(agent.q_table_file):  
        agent.load_q_table()  
    episode_rewards = []  
  
    for episode in range(NUM_EPISODES):  
        total_reward = 0  

        while True:  

            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    pygame.quit()  
                    quit() 

            old_state = agent.get_state(snake, food)  
            action = agent.get_action(old_state)  
    
            # Perform the action and get the reward  
            if action == 0: snake.direction = UP  
            elif action == 1: snake.direction = DOWN  
            elif action == 2: snake.direction = LEFT  
            elif action == 3: snake.direction = RIGHT  
    
            snake.move()  
            
            reward = -0.01  
            done = False  
    
            if snake.get_head_position() == food.position:  
                snake.length += 1  
                reward = 10  # increase the reward for eating food  
                food.randomize_position()  
            elif len(snake.positions) > snake.length:  
                reward = -100  # increase the punishment for dying  
                done = True  
            else:  
                reward = -1  # small negative reward for each step taken  
    
            new_state = agent.get_state(snake, food)  
            agent.update_q_table(old_state, action, reward, new_state, done)  

            total_reward += reward

            if done:  
                break  
    
            screen.fill((0,0,0))  
            snake.draw(screen)  
            food.draw(screen)  
            pygame.display.update()  

            episode_rewards.append(total_reward)  
            agent.decay_epsilon()  
            agent.save_q_table()


            clock.tick(10)  
    
    plt.plot(episode_rewards)  
    plt.show()  

    pygame.quit()  
  
if __name__ == "__main__":  
    main()  
