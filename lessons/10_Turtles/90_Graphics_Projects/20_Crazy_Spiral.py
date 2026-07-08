import turtle
import time

# 1. Screen Setup
win = turtle.Screen()
win.title("Geometry Dash - Python Turtle")
win.bgcolor("lightblue")
win.setup(width=800, height=400)
win.tracer(0) # Turn off automatic updates for smooth animation

# 2. Player (Square)
player = turtle.Turtle()
player.shape("square")
player.color("orange")
player.penup()
player.goto(-250, -100) # Starting position
player.dy = 0 # Jump velocity

# 3. Obstacle (Spike)
obstacle = turtle.Turtle()
obstacle.shape("triangle")
obstacle.color("red")
obstacle.penup()
obstacle.goto(400, -130) # Spawning position off-screen
obstacle.shapesize(1.5, 1.5) # Scale the spike

# 4. Ground Line
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-400, -150)
ground.pendown()
ground.pensize(5)
ground.color("gray")
ground.forward(800)

# 5. Jump Function
def jump():
    if player.ycor() <= -100: # Only jump if on the ground
        player.dy = 15

# Keyboard bindings
win.listen()
win.onkeypress(jump, "space")

# Game Variables
game_running = True
gravity = 0.8
obstacle_speed = 8

# 6. Main Game Loop
while game_running:
    # --- Player Physics ---
    player.dy -= gravity
    player.sety(player.ycor() + player.dy)

    # Floor limit
    if player.ycor() <= -100:
        player.sety(-100)
        player.dy = 0
    
    # --- Obstacle Movement ---
    obstacle.setx(obstacle.xcor() - obstacle_speed)

    # Reset obstacle to the right side of the screen
    if obstacle.xcor() < -400:
        obstacle.setx(400)

    # --- Collision Detection ---
    # Calculate distance between player and the spike (x-axis and y-axis)
    x_dist = abs(player.xcor() - obstacle.xcor())
    y_dist = abs(player.ycor() - obstacle.ycor())
    
    if x_dist < 20 and y_dist < 20:
        game_running = False # Game over!
        print("Game Over! You hit a spike.")

    win.update()
    time.sleep(0.016) # Roughly 60 FPS

win.mainloop()
