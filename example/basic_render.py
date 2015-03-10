#/usr/bin/env python

import pyglet
from json_map import Map

window = pyglet.window.Window()

# load the map
fd = pyglet.resource.file("map.json", 'rt')
m = Map.load_json(fd)

# set the viewport to the window dimensions
m.set_viewport(0, 0, window.width, window.height)

# perform some queries to the map data!

# list all the objects
print("listing all the objects:")
for obj in m.objectgroups["Objects"]:
    print(obj)

# is there a "Door1" object?
print("Door1" in m.objectgroups["Objects"])

# is there aan object in coords 10, 10?
print((0, 10) in m.objectgroups["Objects"])

# get the object named "Door1"
print("Door1:", m.objectgroups["Objects"]["Door1"])

# get the object in coords (5, 3)
print("Obj ar (5, 3)", m.objectgroups["Objects"][5, 3])

# list all the objects with type "Door":
print("listing all the Door objects:")
for obj in m.objectgroups["Objects"].get_by_type("Door"):
    print(obj)

@window.event
def on_draw():
    window.clear()
    m.draw()

pyglet.app.run()
