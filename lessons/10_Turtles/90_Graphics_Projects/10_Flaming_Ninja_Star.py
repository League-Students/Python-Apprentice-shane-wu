import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)

tina.speed(0)

def fractal_triangle(size,depth):
    if depth == 0:
        for i in range(3):
            tina.forward(size)
            tina.left(120)
    else:
        for i in range(3):
            fractal_triangle(size/2,depth-1)
            tina.forward(size)
            tina.left(120)

fractal_triangle(200,5)


turtle.exitonclick()