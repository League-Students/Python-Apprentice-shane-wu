import turtle
import random
import time

# --- SCREEN SETUP ---
screen = turtle.Screen()
screen.title("Galaga Clone (Python Turtle)")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)  # Turns off auto-updates for buttery smooth animations

# --- GAME VARIABLES ---
score = 0
lives = 3
game_is_running = True

# --- PLAYER (SHIP) ---
player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.goto(0, -350)
player.setheading(90)  # Face upward
player_speed = 20

# --- CONTAINERS FOR GAME OBJECTS ---
bullets = []
enemies = []

# --- SCOREBOARD ---
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-280, 360)

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}   Lives: {lives}", align="left", font=("Courier", 16, "bold"))

update_scoreboard()

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

# --- FIRE BULLET FUNCTION ---
def fire_bullet():
    # Limit maximum onscreen bullets to prevent performance drops
    if len(bullets) < 5:
        bullet = turtle.Turtle()
        bullet.shape("square")
        bullet.shapesize(stretch_wid=0.5, stretch_len=0.1) # Makes it look like a laser
        bullet.color("yellow")
        bullet.penup()
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullets.append(bullet)

# --- KEYBOARD BINDINGS ---
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

# --- ENEMY SPAWNER ---
def spawn_enemy():
    enemy = turtle.Turtle()
    enemy.shape("turtle")
    enemy.color("red")
    enemy.penup()
    # Random position along the top boundary
    x = random.randint(-270, 270)
    y = random.randint(200, 330)
    enemy.goto(x, y)
    enemy.setheading(270) # Face downward
    
    # Store custom properties directly in the turtle object
    enemy.speed_x = random.choice([-2, -1, 1, 2])
    enemy.speed_y = -1.5 
    enemies.append(enemy)

# Initial wave deployment
for _ in range(8):
    spawn_enemy()

# --- MAIN GAME LOOP ---
while game_is_running:
    time.sleep(0.01) # Keeps the loop from eating 100% CPU resource
    
    # 1. Handle Bullet Mechanics
    for bullet in bullets[:]:
        bullet.sety(bullet.ycor() + 12)
        # Remove bullet if it leaves the upper boundary
        if bullet.ycor() > 400:
            bullet.hideturtle()
            bullets.remove(bullet)

    # 2. Handle Enemy Mechanics & AI Grid Movement
    for enemy in enemies[:]:
        # Sideways oscillating motion
        enemy.setx(enemy.xcor() + enemy.speed_x)
        # Gradual downward approach
        enemy.sety(enemy.ycor() + enemy.speed_y)

        # Bounce enemies off vertical walls
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            enemy.speed_x *= -1

        # Check if enemy breached defense line
        if enemy.ycor() < -380:
            enemy.goto(random.randint(-270, 270), random.randint(200, 330))

        # 3. Collision Detection (Bullet vs Enemy)
        for bullet in bullets[:]:
            if enemy.distance(bullet) < 20: # 20 pixels bounding box check
                score += 100
                update_scoreboard()
                
                # Cleanup bullet
                bullet.hideturtle()
                if bullet in bullets:
                    bullets.remove(bullet)
                
                # Respawn the hit alien near the top
                enemy.goto(random.randint(-270, 270), random.randint(200, 330))
                enemy.speed_y -= 0.2 # Make subsequent spawns slightly faster

        # 4. Collision Detection (Enemy vs Player Ship)
        if enemy.distance(player) < 25:
            lives -= 1
            update_scoreboard()
            enemy.goto(random.randint(-270, 270), random.randint(200, 330))
            
            if lives <= 0:
                game_is_running = False

    # 5. Refresh Screen Layout Matrix
    screen.update()

# --- GAME OVER SCREEN ---
game_over = turtle.Turtle()
game_over.color("red")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)
game_over.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

screen.update()
screen.mainloop()
