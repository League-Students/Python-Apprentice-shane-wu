import turtle

tina = turtle.Turtle()

screen = turtle.Screen()
screen.setup(500,500)

cam_colors = ["white", "blue", "red", "black", "green"]

def open_cam_1():
    print("cam 1 open")
    screen.bgcolor(cam_colors[0])

def open_cam_2():
    print("cam 2 open")
    screen.bgcolor(cam_colors[1])


screen.listen()
screen.onkey(open_cam_1, "1")
screen.onkey(open_cam_2, "2")





turtle.exitonclick()