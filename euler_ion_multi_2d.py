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
earth.color("blue")
earth.penup()

earth_angle = 0
earth_angular_speed = 2 * math.pi / 365.24

mars = turtle.Turtle()
mars.shape("circle")
mars.color("red")
mars.penup()

mars_angle = math.pi / 2
mars_angular_speed = 2 * math.pi / 686.98

ion_rocket_m = turtle.Turtle()
ion_rocket_m.color("white")
ion_rocket_m.penup()

ion_m_x = 149.5978707e9 # 10^9 m = 1 px
ion_m_y = 0
ion_m_vx = 0
ion_m_vy = 29780
ion_rocket_m.setheading(90)
ion_m_angle = math.pi / 2
n = 150
ion_m_dry_mass = 1e5 + 144 * n
ion_m_rocket_mass = (1e5 + 144 * n) * math.e ** (5580 / 29430)
ion_m_fuel_mass = 100000
ion_m_exhaust_mass = (0.236 / 29430) * n * time_step # 0.693 * n (current)

G = 6.6743e-11
sun_mass = 1.989e30

while True:
    print(current_time, " ", ion_m_fuel_mass)

    earth.goto(149.5978707 * math.cos(earth_angle), 149.5978707 * math.sin(earth_angle))
    mars.goto(227.94 * math.cos(mars_angle), 227.94 * math.sin(mars_angle))

    ion_rocket_m.goto(ion_m_x / 1e9, ion_m_y / 1e9)

    earth.pendown()
    mars.pendown()
    ion_rocket_m.pendown()

    ion_rocket_m.setheading(ion_m_angle * 180 / math.pi)

    if ion_m_fuel_mass > 0:
        ion_m_vx += ion_m_exhaust_mass * 29430 * math.cos(ion_m_angle) / ion_m_rocket_mass
        ion_m_vy += ion_m_exhaust_mass * 29430 * math.sin(ion_m_angle) / ion_m_rocket_mass
        ion_m_fuel_mass -= ion_m_exhaust_mass
        ion_rocket_mass = ion_m_fuel_mass + ion_m_dry_mass

    ion_ax = -(G * sun_mass * ion_m_x) / (ion_m_x ** 2 + ion_m_y ** 2) ** (3 / 2)
    ion_ay = -(G * sun_mass * ion_m_y) / (ion_m_x ** 2 + ion_m_y ** 2) ** (3 / 2)

    ion_m_vx += ion_ax * time_step
    ion_m_vy += ion_ay * time_step

    ion_m_x += ion_m_vx * time_step
    ion_m_y += ion_m_vy * time_step

    current_time += time_step / 86400

    earth_angle += earth_angular_speed * time_step / 86400
    mars_angle += mars_angular_speed * time_step / 86400
    ion_m_angle = math.atan2(ion_m_y, ion_m_x) + math.pi / 2

    screen.update()