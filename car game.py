from ursina import *

app = Ursina()

window.title = "Simple 3D Car Game"

# -------------------------
# Sky
# -------------------------
Sky()

# -------------------------
# Ground
# -------------------------
ground = Entity(
    model='plane',
    scale=(20,1,50),
    texture='white_cube',
    texture_scale=(20,20),
    color=color.green,
    
)

# -------------------------
# Road
# -------------------------
road = Entity(
    model='plane',
    scale=(8,1,50),
    texture='white_cube',
    color=color.gray,
    position=(0,0.01,0)
)
for i in range (-22,23,4):
    Entity(
        model="cube",
        color=color.white,
        scale=(0.3,0.5,2),
        position=(0,0.01,i)
    )
for y in range (-20,21,7):
    Entity(
        model="cube",
        color=color.brown,
        scale=(0.5,3.5,0.5),
        position=(-5,0.01,y)
    )
    Entity(
        model="sphere",
        color=color.green,
        scale=(2,2,2),
        position=(-5,2.8,y)
    )
    Entity(
            model="cube",
            color=color.brown,
            scale=(0.5,3.5,0.5),
            position=(5,0.01,y)
        )
    Entity(
        model="sphere",
        color=color.green,
        scale=(2,2,2),
        position=(5,2.8,y)
    )
for x in range (-20,21,10):
    Entity(
        model="cube",
        color=color.blue,
        scale=(2,5,3),
        position=(8,3,x)
        )
for x in range (-20,21,10):
    Entity(
        model="cube",
        color=color.red,
        scale=(2,5,3),
        position=(-8,3,x)
        )
car = Entity(
    # model='images/sedan.obj',
    model="cube",
    color=color.red,
    scale=(1,0.5,2),
    position=(0,0.5,-18),
    collider='box'
)
obstacle = Entity(
    # model='images/sedan.obj',
    model="cube",
    color=color.black,
    scale=(1,1,1),
    position=(0,0.5,-10),
    collider='box'
)
obstacle2 = Entity(
    # model='images/sedan.obj',
    model="cube",
    color=color.black,
    scale=(1,1,1),
    position=(1,0.5,-5),
    collider='box'
)
obstacle3 = Entity(
    # model='images/sedan.obj',
    model="cube",
    color=color.black,
    scale=(1,1,1),
    position=(-1,0.5,5),
    collider='box'
)
obstacle4 = Entity(
    # model='images/sedan.obj',
    model="cube",
    color=color.black,
    scale=(1,1,1),
    position=(2,0.5,10),
    collider='box'
)
obstacle5 = Entity(
    # model='images/sedan.obj',
    model="cube",
    color=color.black,
    scale=(1,1,1),
    position=(-2,0.5,15),
    collider='box'
)
# -------------------------
# Finish Line
# -------------------------
finish = Entity(
    model='cube',
    color=color.yellow,
    scale=(8,1,2),
    position=(0,0.05,18),
    collider='box'
)

# -------------------------
# Camera
# -------------------------
camera.position = (0,15,-20)
camera.look_at(car)
# camera.rotation_x = 35

# -------------------------
# UI
# -------------------------
lap = 0

speed = 0
max_speed = 15
acceleration = 10
brake = 15
friction = 5

lap_text = Text(
    text="Lap : 0",
    x=-0.85,
    y=0.45,
    scale=2
)

message = Text(
    text="",
    origin=(0,0),
    scale=3,
    color=color.red
)

speed_text = Text(
    text="Lap : 0",
    x=-0.85,
    y=0.35,
    scale=2
)

game_over = False

# -------------------------
# Restart
# -------------------------
def restart():
    global lap, game_over,speed

    lap = 0
    game_over = False

    car.position = (0,0.5,-18)
    car.rotation_y = 0

    lap_text.text = "Lap : 0"
    message.text = ""
    speed = 0

# -------------------------
# Keyboard
# -------------------------
def input(key):

    if key == "r":
        restart()

    if key == "escape":
        application.quit()

# -------------------------
# Update
# -------------------------
def update():

    global lap,speed
    global game_over

    if game_over:
        return

    speed_text.text = f"Speed: {int(speed)}"

    # Move Forward
    # if held_keys["up arrow"]:
    #     car.position += car.forward * 8 * time.dt

    # # Move Backward
    # if held_keys["down arrow"]:
    #     car.position -= car.forward * 5 * time.dt

    if held_keys["up arrow"]:
        speed += acceleration * time.dt

        if speed > max_speed:
            speed = max_speed

# -------------------------
# Braking
# -------------------------

    elif held_keys["down arrow"]:
        speed -= brake * time.dt

    else:
        if speed > 0:
            speed -= friction * time.dt

        if speed < 0:
            speed += friction * time.dt

# Prevent very small values
    if abs(speed) < 0.1:
        speed = 0

# Move car
    car.position += car.forward * speed * time.dt

    # Turn Left
    if held_keys["left arrow"]:
        car.rotation_y -= 80 * time.dt

    # Turn Right
    if held_keys["right arrow"]:
        car.rotation_y += 80 * time.dt

    # Camera Follow
    camera.position = car.position + Vec3(0,15,-20)
    camera.look_at(car)

    # Keep Car on Road
    car.x = clamp(car.x,-3,3)

    # Finish Line
    if car.intersects(finish).hit:

        lap += 1
        lap_text.text = f"Lap : {lap}"

        car.position = (0,0.5,-18)

        if lap == 3:
            message.text = "YOU WIN!"
            game_over = True

    # collision with obstacle
    if car.intersects(obstacle).hit or car.intersects(obstacle2).hit or car.intersects(obstacle3).hit or car.intersects(obstacle4).hit or car.intersects(obstacle5).hit:
        message.text = "Game Over"
        game_over = True

app.run()