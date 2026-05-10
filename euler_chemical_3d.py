# VPython 3.2
from vpython import *
import math

scene.caption = """Hold Ctrl = Rotate
Scroll Wheel = Zoom
Hold Shift = Move
*Planets not up to scale*"""

G = 6.67e-11

sun = sphere(pos=vector(0, 0, 0), radius=1.495978707e11 / 5, color=color.yellow, mass=1.9885e30, emissive=True)

earth = sphere(pos=vector(1.495978707e11, 0, 0), radius=1.495978707e11 / 15, make_trail=True, texture=textures.earth)
earth.v = vector(0, 2.978e4, 0)
earth_angle = 0
earth_angular_speed = 2 * math.pi / (365.24 * 24)

mars_angle = 0.773180858633 # 44.3 deg
mars = sphere(pos=vector(2.28e11 * math.sin(mars_angle), 2.28e11 * math.cos(mars_angle), 0), radius=1.495978707e11 / 15, color=color.red, make_trail=True) #1.52 * AU
mars.v = vector(-2.41e4 * math.cos(mars_angle), 2.41e4 * math.sin(mars_angle), 0)
mars_angular_speed = 2 * math.pi / (686.98 * 24)

rocket = cylinder(pos=vector(1.495978707e11, 0, 0), radius=1.495978707e11 / 10, color=color.orange, make_trail=True, mass=5e5)
rocket.v = vector(0, 2.978e4, 0)

current_time = 0
time_step = 1 * 3600 # hours

while True:
    rate(500)

    print(f"Time: {current_time / 86400}") # days

    earth.pos = vector(1.495978707e11 * math.cos(earth_angle), 1.495978707e11 * math.sin(earth_angle), 0)
    mars.pos = vector(2.28e11 * math.cos(mars_angle), 2.28e11 * math.sin(mars_angle), 0)

    rocket.a = -G * sun.mass * norm(rocket.pos) / mag(rocket.pos) ** 2
    rocket.v += rocket.a * time_step
    rocket.pos += rocket.v * time_step

    if rocket.mass > 256884:
        rocket.v.y += 4414.5 * math.log(5e5 / 256883.072466, math.e)
        rocket.mass -= 243117

    if rocket.mass == 256883 and rocket.v.x > 0:
        rocket.v.y -= 4414.5 * math.log(256883.072466 / 140845, math.e)
        rocket.mass -= 116038

    earth_angle += earth_angular_speed * time_step / 3600
    mars_angle += mars_angular_speed * time_step / 3600

    current_time += time_step