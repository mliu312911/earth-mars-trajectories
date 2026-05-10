# VPython 3.2
from vpython import *
import math

scene.caption = """Hold Ctrl = Rotate
Scroll Wheel = Zoom
Hold Shift = Move
*Planets not up to scale*"""

current_time = 0
time_step = 1 * 3600 # hours

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

rocket_angle = math.pi / 2
dry_mass = 500 / math.e ** (5580 / 29430) #413.6 #439.434 for 3800 delta v # 4000 perfect?? # difference in orbital vel = 5680
rocket_mass = 500
fuel_mass = rocket_mass - dry_mass #86.4 #60.566
exhaust_mass = (0.091 / 29430) * time_step # NEXT = 0.236 N # 0.693 kg/day (current) #0.08 for 0.236 mass

while True:
    rate(500)

    print(f"Time: {current_time / 86400}") # days

    earth.pos = vector(1.495978707e11 * math.cos(earth_angle), 1.495978707e11 * math.sin(earth_angle), 0)
    mars.pos = vector(2.28e11 * math.cos(mars_angle), 2.28e11 * math.sin(mars_angle), 0)

    rocket.a = -G * sun.mass * norm(rocket.pos) / mag(rocket.pos) ** 2
    rocket.v += rocket.a * time_step
    rocket.pos += rocket.v * time_step

    if rocket.mass > 0:
        rocket.v.x += exhaust_mass * 29430 * math.cos(rocket_angle) / rocket_mass
        rocket.v.y += exhaust_mass * 29430 * math.sin(rocket_angle) / rocket_mass
        rocket.mass -= exhaust_mass

    earth_angle += earth_angular_speed * time_step / 3600
    mars_angle += mars_angular_speed * time_step / 3600
    rocket_angle = math.atan2(rocket.pos.y, rocket.pos.x) + math.pi / 2

    current_time += time_step