"""
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables.
"""

import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.pencolor('blue')

from pathlib import Path                        # Import Path from pathlib module
    image_dir = Path('leaguebot_bot.gif').parent.parent / "images"    # Define the directory containing images
    image_path = str(90 / 'leaguebot_bot.gif')  

... # Your Code Here