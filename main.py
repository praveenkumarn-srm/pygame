# from ursina import *
# app = Ursina()

# cube=Entity(
#     model="cube",
#     color=color.orange,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.pink,
#     scale=(4,3,2),
#     position=(0,2,3),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.brown,
#     scale=(2,3,4),
#     position=(-4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.violet,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.cyan,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.green,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.lime,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.gray,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.salmon,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.peach,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.violet,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.light_gray,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.dark_gray,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )

# cube=Entity(
#     model="cube",
#     color=color.red,
#     scale=(2,3,4),
#     position=(4,2,1),
#     rotation=(45,45,45)
# )


# cube=Entity(
#     model="cube",
#     color=color.blue,
#     x=-3
# )
# cube=Entity(
#     model="sphere",
#     color=color.red
# )
# cube=Entity(
#     model="plane",
#     color=color.yellow,
#     x=3
# )
# cube=Entity(
#     model="circle",
#     color=color.black,
#     y=3
# )
# cube=Entity(
#     model="quad",
#     color=color.white,
#     y=-3
# )
# def update():
#     cube.rotation_x=cube.rotation_x+5

# EditorCamera()

# app.run()






from ursina import *
app=Ursina()
# cube=Entity(
#     model="cube",
#     color=color.blue,
#     collider="box"
# )
# coin=Entity(
#     model="sphere",
#     color=color.yellow,
#     x=5,
#     collider="box"
# )
# def update():
#     cube.rotation_z+=10

# def input(key):
#     if key == "a":
#         cube.x=cube.x-2
#     if key == "w":
#         cube.z=cube.z+2
#     if key == "s":
#         cube.z=cube.z-2
#     if key == "d":
#         cube.x=cube.x+2
#     if key == "space":
#         cube.y=cube.y+2
#     if key == "c":
#         cube.y=cube.y-2
# Button(
#     text="click",
#     scale=(0.5,0.5,0.5),
#     #model="sphere",
#     color=color.red,
#     text_size=2,
#     text_color=color.blue
# )


# def update():
#     if held_keys["w"]:
#         cube.z+=0.1
#     if held_keys["a"]:
#         cube.x-=0.1
#     if held_keys["s"]:
#         cube.z-=0.1
#     if held_keys["d"]:
#         cube.x+=0.1

cube=Entity(
    model="cube",
    color=color.gray,
    scale=(1,2,1),
    y=1.5
)

cube2=Entity(
    model="cube",
    color=color.gray,
    scale=(0.3,3,1),
)

circle=Entity(
    model="sphere",
    color=color.red,
    scale=(1,1,1),
    y=2.5,
    z=-1
)

circle1=Entity(
    model="sphere",
    color=color.yellow,
    scale=(1,1,1),
    y=2,
    z=-1
)

circle2=Entity(
    model="sphere",
    color=color.green,
    scale=(0.5,0.5,0.5),
    y=1.5,
    z=-1
)
    
def red_signal():
    circle.color = color.red
    circle1.color = color.light_gray
    circle2.color = color.light_gray

    invoke(yellow_signal,delay=3)

def yellow_signal():
    circle.color = color.light_gray
    circle1.color = color.yellow
    circle2.color = color.light_gray

    invoke(green_signal,delay=3)


def green_signal():
    circle.color = color.light_gray
    circle1.color = color.light_gray
    circle2.color = color.green

    invoke(red_signal,delay=3)

red_signal()

# Text(text="welcome to my first cube creation",y=0,rotation_x=45)
# text=Text(text="score=0",x=-0.85,y=0.45,scale=2,color=color.blue,background=True)
# text.background.color=color.red
EditorCamera()
app.run()