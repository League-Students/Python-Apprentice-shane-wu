import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina_path = [1,2,3,4,5]
tina_progress = 0

screen = turtle.Screen()
screen.setup(500,500)


cam_colors = ["white", "blue", "red", "black", "green"]

def show_animatronics(cam_num):
    if()


def open_cam_1():
    print("cam 1 open")
    screen.bgcolor(cam_colors[0])

def open_cam_2():
    print("cam 2 open")
    screen.bgcolor(cam_colors[1])

def open_cam_3():
    print("cam 3 open")
    screen.bgcolor(cam_colors[2])

def open_cam_4():
    print("cam 4 open")
    screen.bgcolor(cam_colors[3])

def open_cam_5():
    print("cam 5 open")
    screen.bgcolor(cam_colors[4])

def exit_cam():
    print("cam exited")
    screen.bgcolor("yellow")


screen.listen()
screen.onkey(open_cam_1, "1")
screen.onkey(open_cam_2, "2")
screen.onkey(open_cam_3, "3")
screen.onkey(open_cam_4, "4")
screen.onkey(open_cam_5, "5")
screen.onkey(exit_cam, "0")








turtle.exitonclick()