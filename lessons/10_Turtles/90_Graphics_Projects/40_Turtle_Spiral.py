import turtle
import random

# --- GAME SETUP ---
screen = turtle.Screen()
screen.title("Python Galaga")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)  # Turns off automatic screen updates for smooth animation

# --- GAME VARIABLES ---
player_speed = 20
laser_speed = 15
alien_speed = 2
laser_state = "ready"  # "ready" means can fire, "firing" means laser is on screen

# --- CREATE GAME ENTITIES ---
# Player Ship
player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("cyan")
player.penup()
player.goto(0, -350)
player.setheading(90)  # Point upwards

# Player Laser
laser = turtle.Turtle()
laser.speed(0)
laser.shape("square")
laser.shapesize(stretch_wid=0.5, stretch_len=0.1)
laser.color("yellow")
laser.penup()
laser.hline = 0
laser.hideturtle()

# Score Display
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-280, 360)
score_display.write(f"Score: {score}", font=("Courier", 16, "normal"))

# Alien Fleet
aliens = []
# Create a grid of 5 rows and 8 columns of aliens
for row in range(5):
    for col in range(8):
        alien = turtle.Turtle()
        alien.speed(0)
        alien.shape("circle")
        alien.color("red")
        alien.penup()
        # Position aliens in a grid layout
        x = -200 + (col * 50)
        y = 200 + (row * 30)
        alien.goto(x, y)
        aliens.append(alien)

# --- PLAYER MOVEMENT FUNCTIONS ---
def move_left():
    x = player.xcor() - player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor() + player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire_laser():
    global laser_state
    if laser_state == "ready":
        laser_state = "firing"
        # Move laser to just above the player ship
        laser.goto(player.xcor(), player.ycor() + 10)
        laser.showturtle()

# --- KEYBOARD BINDINGS ---
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_laser, "space")

# --- MAIN GAME LOOP ---
game_running = True

while game_running:
    screen.update()  # Manually refresh the screen graphics

    # 1. Move the player's laser
    if laser_state == "firing":
        laser.sety(laser.ycor() + laser_speed)
        # Reset laser if it flies off the top of the screen
        if laser.ycor() > 390:
            laser.hideturtle()
            laser_state = "ready"

    # 2. Move and manage the aliens
    for alien in aliens:
        # Subtle horizontal weaving using the random module
        alien.setx(alien.xcor() + random.choice([-2, 0, 2]))
        # Constant descent towards the player
        alien.sety(alien.ycor() - alien_speed)

        # Collision check: Laser hits an Alien
        if laser_state == "firing" and laser.distance(alien) < 20:
            laser.hideturtle()
            laser_state = "ready"
            laser.goto(0, 1000)  # Move active laser out of bounds
            alien.goto(1000, 1000)  # Move dead alien off-screen
            aliens.remove(alien)
            
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", font=("Courier", 16, "normal"))
            break

        # Collision check: Alien hits Player (Game Over)
        if alien.distance(player) < 20 or alien.ycor() < -380:
            game_running = False
            score_display.goto(-100, 0)
            score_display.write("GAME OVER", font=("Courier", 30, "bold"))
            break

    # Win Condition: All aliens destroyed
    if not aliens:
        game_running = False
        score_display.goto(-100, 0)
        score_display.write("YOU WIN!", font=("Courier", 30, "bold"))

# Keep the window open after the game ends
screen.mainloop()
