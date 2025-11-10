#test snake game (own work)
import os
import random
import time

#configuration for the width height and speed, defines how big the board will be, 20 columns wide and 10 rows tall
WIDTH = 20
HEIGHT = 10
SPEED = 0.2

#snake and food, the snake is a list of x, y coordinates, the food is one random coordrinate
snake = [(5, 5)]
direction = "RIGHT"
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))

def clear():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw():
    """Draws the board, snake, and food."""
    clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print ("0", end="") #snakes body
            elif (x, y) == food:
                print("@", end="") #food
            else:
                print(" ", end="") #empty space thats not the snake or the food
        print()
    print(f"score: {len(snake) - 1}")

def move():
    """moves the snake by changing its head position."""
    global food
    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= 1
    elif direction == "DOWN":
        head_y += 1
    elif direction == "LEFT":
        head_x -= 1
    elif direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)
    #checking for collisions with the wall or yourself
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake
    ):
        return False    #game over
    
    snake.insert(0, new_head)   #move head

    #check for eating food during game
    if new_head == food:
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        snake.pop() #removes tail if no food eaten

    return True #still alive

def get_input():
    """Gets player input (WASD)."""
    global direction
    move_dir = input("Move (W/A/S/D): ").strip().upper()
    if move_dir == "W" and direction != "DOWN":
        direction = "UP"
    elif move_dir == "S" and direction != "UP":
        direction = "DOWN"
    elif move_dir == "A" and direction != "RIGHT":
        direction = "LEFT"
    elif move_dir == "D" and direction != "LEFT":
        direction = "RIGHT"

# MAIN LOOP
while True:
    draw()
    if not move():
        clear()
        print("Game Over lol!")
        print(f"Final Score: {len(snake) - 1}")
        break
    time.sleep(SPEED)
    get_input()
