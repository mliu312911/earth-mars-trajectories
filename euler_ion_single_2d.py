import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

current_time = 0
time_step = 1 * 86400

sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2)

sun_label = turtle.Turtle()
sun_label.hideturtle()
sun_label.color("yellow")
sun_label.penup()
sun_label.goto(0, 25)
sun_label.write("Sun", align="center", font=("Arial", 16, "normal"))

earth = turtle.Turtle()
earth.shape("circle")
earth.color("dark turquoise")
earth.penup()

earth_angle = 0
earth_angular_speed = 2 * math.pi / 365.24

mars = turtle.Turtle()
mars.shape("circle")
mars.color("red")
mars.penup()

mars_angle = math.pi / 2
mars_angular_speed = 2 * math.pi / 686.98

ion_rocket = turtle.Turtle()
ion_rocket.color("white")
ion_rocket.shapesize(1.25)
ion_rocket.penup()

ion_x = 149.5978707e9 # 10^9 m = 1 px
ion_y = 0
ion_vx = 0
ion_vy = 29780
ion_rocket.setheading(90)
ion_angle = math.pi / 2
ion_dry_mass = 500 / math.e ** (5580 / 29430) #413.6 #439.434 for 3800 delta v # 4000 perfect?? # difference in orbital vel = 5680
ion_rocket_mass = 500
ion_fuel_mass = ion_rocket_mass - ion_dry_mass #86.4 #60.566
ion_exhaust_mass = (0.236 / 29430) * time_step # NEXT = 0.236 N # 0.693 kg/day (current) #0.08 for 0.236 mass

G = 6.6743e-11
sun_mass = 1.989 * 10 ** 30

while True:
    print(current_time, " ", ion_fuel_mass)

    earth.goto(149.5978707 * math.cos(earth_angle), 149.5978707 * math.sin(earth_angle))
    mars.goto(227.94 * math.cos(mars_angle), 227.94 * math.sin(mars_angle))

    ion_rocket.goto(ion_x / 1e9, ion_y / 1e9)

    earth.pendown()
    mars.pendown()
    ion_rocket.pendown()

    ion_rocket.setheading(ion_angle * 180 / math.pi)

    if ion_fuel_mass > 0:
        ion_vx += ion_exhaust_mass * 29430 * math.cos(ion_angle) / ion_rocket_mass
        ion_vy += ion_exhaust_mass * 29430 * math.sin(ion_angle) / ion_rocket_mass
        ion_fuel_mass -= ion_exhaust_mass
        ion_rocket_mass = ion_fuel_mass + ion_dry_mass

    ion_ax = -(G * sun_mass * ion_x) / (ion_x ** 2 + ion_y ** 2) ** (3 / 2)
    ion_ay = -(G * sun_mass * ion_y) / (ion_x ** 2 + ion_y ** 2) ** (3 / 2)

    ion_vx += ion_ax * time_step
    ion_vy += ion_ay * time_step

    ion_x += ion_vx * time_step
    ion_y += ion_vy * time_step

    current_time += time_step / 86400

    earth_angle += earth_angular_speed * time_step / 86400
    mars_angle += mars_angular_speed * time_step / 86400
    ion_angle = math.atan2(ion_y, ion_x) + math.pi / 2

    screen.update()