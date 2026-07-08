import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)

def fractal_triangle(size,depth):
    if depth == 0:
        for i in range(3):
            tina.forward(size)
            tina.left(120)
    else:
        for i in range(3):
            fractal_triangle()

fractal_triangle(200,0)


turtle.exitonclick()