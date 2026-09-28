from ursina import *
app = Ursina()
score = 0
lives=3
game_over=False

paddle=Entity( 
    model="cube",
    color=color.green,
    scale=(2,0.5,1),
    position=(0,-3,0),
    collider="box"
)

ball=Entity( 
    model="sphere",
    color=color.red,
    scale=(0.5,0.5,0.5),
    position=(0,-2.5,0),
    collider="sphere"
)

text=Text(
    text="Score:0",
    x=-0.89,
    y=0.5,
    scale=2
)

text1=Text(
    text="Lives:3",
    x=0.68,
    y=0.5,
    scale=2
)

text2=Text(
    text="",
    origin=(0,0),
    scale=3
)

ball.dx=5
ball.dy=5

bricks=[]

colors=[
    color.red,
    color.orange,
    color.yellow,
    color.green,
    color.azure,
    color.violet
]

for row in range(6):
    for col in range(8):
        brick=Entity(
        model="cube",
        scale=(1.5,0.5,1),
        color=colors[row],
        position=(col*1.8-6.3,3.7-row*0.7,0),
        collider="box"
        )
        bricks.append(brick)

def reset_ball():
    ball.position=(0,-2.5,0)
    ball.dx=5
    ball.dy=5

def restart():
    global score
    global lives,game_over
    if game_over == False:
        return
    for row in range(6):
        for col in range(8):
            brick=Entity(
            model="cube",
            scale=(1.5,0.5,1),
            color=colors[row],
            position=(col*1.8-6.3,3.7-row*0.7,0),
            collider="box"
        )
        bricks.append(brick)
    text2.text = ""
    ball.x=ball.x+ball.dx*time.dt
    ball.y=ball.y+ball.dy*time.dt
    text1.text=f"Lives:{lives}"
    reset_ball()
    if held_keys["left arrow"]:
        paddle.x-=8 * time.dt
    if held_keys["right arrow"]:
        paddle.x+=8 * time.dt

def update():
    global score
    global lives,game_over

    if game_over == True:
        return

    if held_keys["left arrow"]:
        paddle.x-=8 * time.dt
    if held_keys["right arrow"]:
        paddle.x+=8 * time.dt
    paddle.x=clamp(paddle.x,-6.1,6.1)
    ball.x=ball.x+ball.dx*time.dt
    ball.y=ball.y+ball.dy*time.dt
    #left
    if ball.x<=-7:
        ball.dx=ball.dx*-1
    #right
    if ball.x>=7:
        ball.dx=ball.dx*-1
    #top
    if ball.y>=4:
        ball.dy=ball.dy*-1
    if ball.intersects(paddle).hit and ball.dy<0:
        ball.dy=ball.dy*-1
    for brick in bricks[:]:
        if ball.intersects(brick).hit:
            destroy(brick)
            bricks.remove(brick)
            ball.dy=ball.dy*-1
            score=score+1
            text.text=f"Score:{score}"
    if ball.y<-4:
        lives=lives-1
        text1.text=f"Lives:{lives}"
        if lives==0:
            text2.text = "Game over\nPress R to restart"
            game_over=True
        else:
            reset_ball()
    if len(bricks)==0:
        text2.text = "You WIN\nPress R to continue"

def input(key):
    if key == "r":
        restart()

EditorCamera()
app.run()
