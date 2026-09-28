from ursina import *
app=Ursina()

window.title = "runner"

Sky()
score = 0
game_over = False
distance = 0
speed = 10

obs_sound=Audio("obstacle_sound.mp3",autoplay=False)
coin_sound=Audio("coin_sound.mp3",autoplay=False)

window.color = color.rgb(255, 255, 255)

ground = Entity(
    model="plane",
    color=color.green,
    scale=(10,1,100),
    texture= "white_cube",
    texture_scale=(30,80)
)

player = Entity(
    model="cube",
    color=color.orange,
    scale=(1,2.4,1),
    position=(0,0.8,0),
    collider="box"
)

text = Text(
    text="Score:0",
    x=-0.89,
    y=0.5,
    scale=2
)

message = Text(
    text="",
    origin=(0,0),
    scale=2,
    color=color.red
)

text1 = Text(
    text="Distance:0",
    x=0.5,
    y=0.5,
    scale=2
)

lanes=[-2,0,2]
obstacles=[]
lane=random.choice(lanes)
for y in range (5):
    obstacle = Entity(
    model = "cube",
    color = color.red,
    scale = (0.85,2,1),
    position = (lane,1,20+y*12),
    collider = "box"
    )
    obstacles.append(obstacle)  

coins=[]
for ya  in range(5):

    coin = Entity(
        model="sphere",
        color=color.yellow,
        scale=(0.5,0.5,0.5),
        position=(
            random.choice(lanes),
            1.5,
            30+ya*18
        ),
        collider="sphere"
    )
    coins.append(coin)

def update():

    global score,game_over,distance,speed

    if game_over:
        return

    if held_keys["left arrow"]:
        player.x-=5 * time.dt
    if held_keys["right arrow"]:
        player.x+=5 * time.dt

    player.x = clamp(player.x,-2,2)

    for obstacle in obstacles:

        obstacle.z -= speed * time.dt

        if obstacle.z < -speed:
            obstacle.z = random.randint(50,70)
            obstacle.x = random.choice(lanes)

        if player.intersects(obstacle).hit:
            message.text = "Game over"
            game_over=True
            obs_sound.play()

    for coin in coins:
    
        coin.z -= speed * time.dt
    
        if coin.z < -speed:
            coin.z = random.randint(50,70)
            coin.x = random.choice(lanes)
    
        if player.intersects(coin).hit:
            score += 1
            coin.z = random.randint(50,70)
            coin.x = random.choice(lanes)

            text.text=f"Score:{score}"
            coin_sound.play()

    distance+=10*time.dt
    print(distance)
    text1.text=f"Distance:{int(distance)}"

    speed += 0.2*time.dt

camera.position = (0,8,-18)
camera.rotation_x = 25

app.run()