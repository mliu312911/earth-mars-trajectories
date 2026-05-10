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

mars_angle = 44.44 * math.pi / 180 #0.773180858633
mars_angular_speed = 2 * math.pi / 686.98

chem_rocket = turtle.Turtle()
chem_rocket.color("lime")
chem_rocket.shapesize(1.25)
chem_rocket.penup()

chem_x = 149.5978707e9 # 10^9 m = 1 px
chem_y = 0
chem_vx = 0
chem_vy = 29780
chem_rocket.setheading(90)
chem_angle = math.pi / 2
chem_fuel_mass = 359155
chem_dry_mass = 140845
chem_rocket_mass = chem_fuel_mass + chem_dry_mass

G = 6.6743e-11
sun_mass = 1.989e30

while True:
    print(current_time)

    earth.goto(149.5978707 * math.cos(earth_angle), 149.5978707 * math.sin(earth_angle))
    mars.goto(227.94 * math.cos(mars_angle), 227.94 * math.sin(mars_angle))

    chem_rocket.goto(chem_x / 1e9, chem_y / 1e9)
    chem_rocket.setheading(chem_angle * 180 / math.pi)

    earth.pendown()
    mars.pendown()
    chem_rocket.pendown()

    if chem_rocket_mass > 256883:
        chem_vy += 4414.5 * math.log(5e5 / 256883.072466, math.e)
        chem_rocket_mass -= 243117

    if current_time == 259:
        chem_vy -= 4414.5 * math.log(256883.072466 / 140845, math.e)
        chem_rocket_mass -= 116038

    # Chem gravity

    chem_ax = -(G * sun_mass * chem_x) / (chem_x ** 2 + chem_y ** 2) ** (3 / 2)
    chem_ay = -(G * sun_mass * chem_y) / (chem_x ** 2 + chem_y ** 2) ** (3 / 2)

    chem_vx += chem_ax * time_step
    chem_vy += chem_ay * time_step

    chem_x += chem_vx * time_step
    chem_y += chem_vy * time_step

    current_time += time_step / 86400

    earth_angle += earth_angular_speed * time_step / 86400
    mars_angle += mars_angular_speed * time_step / 86400
    chem_angle = math.atan2(chem_y, chem_x) + math.pi / 2

    screen.update()