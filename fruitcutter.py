from ursina import *
app = Ursina()

#variables
score = 0 
lives = 3

fruits = None

fruits_speed_x = 0
fruits_speed_y = 0

gravity = 0.5

game_over = False

#background
background = Entity(
    model="quad",
    scale=(16,9),
    color=color.black,
    z=1
)

#knife
knife = Entity(
    model="quad",
    scale=(0.5,1),
    texture="knife.jpg"
)

#text
score_text = Text(
    text="Score : 0",
    x=-0.89,
    y=0.50,
    scale=2
)

lives_text = Text(
    text="Lives : 3",
    x=-0.89,
    y=0.45,
    scale=2
)

def update():
    knife.x = mouse.position.x
    knife.y = mouse.position.y


app.run()