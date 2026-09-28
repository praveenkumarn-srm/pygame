from ursina import *
app = Ursina()
window.title = "2 Cars Racing Game"

# Sky
Sky()

# Variables
TRACK_RADIUS = 25

INNER_RADIUS = 23
OUTER_RADIUS = 27

MAX_LAPS = 3

race_over = False

# Player variables
player_angle = 0
player_speed = 10
player_lap = 0
player_radius = 25
max_speed = 10
acceleration = 5
brake = 8
friction = 2

# computer variables
computer_angle = 0
computer_speed = 10
computer_lap = 0
computer_radius = 25



# Ground
ground = Entity(
    model='plane',
    scale=(100,1,100),
    # texture='white_cube',
    # texture_scale=(20,20),
    color=color.green
)

# Cars
car1 = Entity(
    model="cube",
    color=color.red,
    scale=(1,0.5,2),
    position=(25,0.5,2.5),
    collider='box'
)

car = Entity(
    model="cube",
    color=color.blue,
    scale=(1,0.5,2),
    position=(25,0.5,5),
    collider='box'
)

# Track
number_of_segments = 100

for i in range(number_of_segments):

    angle = i * (360 / number_of_segments)

    rad = math.radians(angle)

    x = math.cos(rad) * TRACK_RADIUS
    z = math.sin(rad) * TRACK_RADIUS

    Entity(
        model="cube",
        color=color.gray,
        scale=(7, 0.15, 4),
        position=(x, 0.05, z),
        rotation_y=-angle
    )

# Inner Border
for i in range(number_of_segments):

    angle = i * (360 / number_of_segments)

    rad = math.radians(angle)

    x = math.cos(rad) * INNER_RADIUS
    z = math.sin(rad) * INNER_RADIUS

    Entity(
        model="cube",
        color=color.white,
        scale=(1, 0.15, 4),
        position=(x, 0.5, z),
        rotation_y=-angle
    )

# Outer border
for i in range(number_of_segments):

    angle = i * (360 / number_of_segments)

    rad = math.radians(angle)

    x = math.cos(rad) * OUTER_RADIUS
    z = math.sin(rad) * OUTER_RADIUS

    Entity(
        model="cube",
        color=color.white,
        scale=(1, 0.15, 4),
        position=(x, 0.5, z),
        rotation_y=-angle
    )

# Road markings
for i in range(0,number_of_segments,5):

    angle = i * (360 / number_of_segments)

    rad = math.radians(angle)

    x = math.cos(rad) * TRACK_RADIUS
    z = math.sin(rad) * TRACK_RADIUS

    Entity(
        model="cube",
        color=color.white,
        scale=(0.2, 0.2, 2),
        position=(x, 0.15, z),
        rotation_y=-angle
    )

# Finish line
finish = Entity(
    model='cube',
    scale=(7,0.1,1),
    color=color.yellow,
    position=(25,0.15,-2.5),
    rotation_y=90
)

# Trees
for i in range(0,number_of_segments,5):

    angle = i * (360 / number_of_segments)

    rad = math.radians(angle)

    x = math.cos(rad) * 36
    z = math.sin(rad) * 36

    Entity(
        model="cube",
        color=color.brown,
        scale=(0.6, 3, 0.6),
        position=(x, 1.5, z),
    )

    Entity(
        model="sphere",
        color=color.green,
        scale=(3, 3, 3),
        position=(x, 3.5, z),
    )

# Text Messages
player_lap_text = Text(
    text="Player Lap : 0",
    x=-0.89,
    y=0.50,
    scale=2
)

computer_lap_text = Text(
    text="Computer Lap : 0",
    x=-0.89,
    y=0.45,
    scale=2
)

speed_text = Text(
    text="Speed : 0",
    x=-0.89,
    y=0.40,
    scale=2
)

position_text = Text(
    text= "Position : 1 / 2",
    x=-0.89,
    y=0.35,
    scale=2
)

controls_text = Text(
    text= "UP = Accelerate  DOWN = Brake LEFT/RIGHT",
    x=-0.89,
    y=0.30,
    scale=1
)

message = Text(
    text= "",
    origin=(0,0),
    scale=3,
    color=color.yellow
)

# Update functions
def update_player_position():
    rad = math.radians(player_angle)
    
    car1.x = math.cos(rad) * player_radius
    car1.z= math.sin(rad) * player_radius

    car1.rotation_y = -player_angle

def update_computer_position():
    rad = math.radians(computer_angle)
    
    car.x = math.cos(rad) * computer_radius
    car.z= math.sin(rad) * computer_radius

    car.rotation_y = -computer_angle

def update_player_lap():
    global player_lap

    player_lap = int(player_angle //  360)

    if player_lap > MAX_LAPS:
        player_lap = MAX_LAPS
    player_lap_text.text = (
        f"Player Lap : {player_lap} / {MAX_LAPS}"
    )

def update_computer_lap():
    global computer_lap

    computer_lap = int(computer_angle //  360)

    if computer_lap > MAX_LAPS:
        computer_lap = MAX_LAPS
    computer_lap_text.text = (
        f"Computer Lap : {computer_lap} / {MAX_LAPS}"
    )

def update_race_position():
    player_progress = player_angle
    computer_progress = computer_angle
    if player_progress >= computer_progress:
        position_text.text = "Position : 1 / 2"
    else:
        position_text.text = "Position : 2 / 2"

def update():
    global player_angle,computer_angle
    global race_over
    global player_speed,player_radius

    if race_over:
        return

    if held_keys["up arrow"]:
        player_speed += acceleration * time.dt
        #speed_text.text += "Speed : {player_speed}"


        if player_speed > max_speed:
            player_speed = max_speed

    elif held_keys["down arrow"]:
        player_speed -= brake * time.dt 

        if player_speed < 0:
            player_speed = 0

    else:
        if player_speed > 0:
            player_speed -= friction * time.dt 
    
            if player_speed < 0:
                player_speed = 0

    if player_speed > 0:
        player_angle += player_speed * 3 * time.dt

    if held_keys["left arrow"]:
        player_radius -= 5 * time.dt 

    if  held_keys["left arrow"]:
        player_radius += 5 * time.dt 

    player_radius = clamp(
        player_radius,
        INNER_RADIUS + 0.5,
        OUTER_RADIUS - 0.5
    )

    update_player_position()

    #computer movement
    computer_angle += computer_speed * time.dt

    update_computer_position()

    update_player_lap()

    update_computer_lap()

    update_race_position()

    if player_lap == 3:
        message.text = "The Player Wins"
        race_over = True
    elif computer_lap == 3:
        message.text = "The Computer Wins"
        race_over = True
    else:
        message.text = ""
        race_over = False

EditorCamera()
app.run()