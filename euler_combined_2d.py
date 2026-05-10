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

chem_rocket = turtle.Turtle()
chem_rocket.color("lime")
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

ion_rocket = turtle.Turtle()
ion_rocket.color("white")
ion_rocket.penup()

ion_x = 149.5978707e9 # 10^9 m = 1 px
ion_y = 0
ion_vx = 0
ion_vy = 29780
ion_rocket.setheading(90)
ion_angle = math.pi / 2
ion_fuel_mass = 86.4
ion_dry_mass = 413.6
ion_rocket_mass = ion_fuel_mass + ion_dry_mass
ion_exhaust_mass = 0.3 * time_step / 86400 # NSTAR = 0.1 kg/day, NEXT = 0.3 kg/day

ion_rocket_m = turtle.Turtle()
ion_rocket_m.color("magenta")
ion_rocket_m.penup()

ion_m_x = 149.5978707e9 # 10^9 m = 1 px
ion_m_y = 0
ion_m_vx = 0
ion_m_vy = 29780
ion_rocket_m.setheading(90)
ion_m_angle = math.pi / 2
n = 3
ion_m_dry_mass = 1e5 + 144 * n
ion_m_rocket_mass = (1e5 + 144 * n) * math.e ** (5580 / 29430)
ion_m_fuel_mass = ion_m_rocket_mass - ion_dry_mass
ion_m_exhaust_mass = 2.07 * n * time_step / 86400 #.693

G = 6.6743 * 10 ** -11
sun_mass = 1.989 * 10 ** 30

while True:
    earth.goto(149.5978707 * math.cos(earth_angle), 149.5978707 * math.sin(earth_angle))
    mars.goto(227.94 * math.cos(mars_angle), 227.94 * math.sin(mars_angle))

    chem_rocket.goto(chem_x / 1e9, chem_y / 1e9)

    ion_rocket.goto(ion_x / 1e9, ion_y / 1e9)
    #ion_rocket.setheading(ion_angle * 180 / math.pi)

    ion_rocket_m.goto(ion_m_x / 1e9, ion_m_y / 1e9)

    #earth_label.clear()
    #earth_label.goto(149.5978707 * math.cos(earth_angle), 149.5978707 * math.sin(earth_angle) - 30)
    #earth_label.write("Earth", font=("Arial", 16, "normal"))

    earth.pendown()
    mars.pendown()
    chem_rocket.pendown()
    ion_rocket.pendown()
    ion_rocket_m.pendown()

    print(f"Time (Days): {current_time} | Chem Position: ({chem_x}, {chem_y}) | Ion Position ({ion_x}, {ion_y}) | Chem Velocity: {math.sqrt(chem_vx**2 + chem_vy**2)} | Ion Velocity: {math.sqrt(ion_vx**2 + ion_vy**2)}")

    # burns

    if chem_rocket_mass > 256884:
        chem_vy += 4414.5 * math.log(5e5 / 256883.072466, math.e)
        chem_fuel_mass -= 243117
        chem_rocket_mass = chem_fuel_mass + chem_dry_mass

    if chem_vy < 0 and chem_vx == 0:
        chem_vy -= 4414.5 * math.log(256883.072466 / 140845, math.e)
        chem_fuel_mass -= 116038
        chem_rocket_mass = chem_fuel_mass + chem_dry_mass

    # ion thrust

    if ion_fuel_mass > 0:
        ion_vx += ion_exhaust_mass * 29430 * math.cos(ion_angle) / ion_rocket_mass
        ion_vy += ion_exhaust_mass * 29430 * math.sin(ion_angle) / ion_rocket_mass
        ion_fuel_mass -= ion_exhaust_mass
        ion_rocket_mass = ion_fuel_mass + ion_dry_mass

    # ion multiple engine thrust

    if ion_m_fuel_mass > 0:
        ion_m_vx += ion_m_exhaust_mass * 29430 * math.cos(ion_angle) / ion_m_rocket_mass
        ion_m_vy += ion_m_exhaust_mass * 29430 * math.sin(ion_angle) / ion_m_rocket_mass
        ion_m_fuel_mass -= ion_m_exhaust_mass
        ion_m_rocket_mass = ion_m_fuel_mass + ion_m_dry_mass

    # Chem gravity

    chem_ax = -(G * sun_mass * chem_x) / (chem_x ** 2 + chem_y ** 2) ** (3/2)
    chem_ay = -(G * sun_mass * chem_y) / (chem_x ** 2 + chem_y ** 2) ** (3/2)

    chem_vx += chem_ax * time_step
    chem_vy += chem_ay * time_step

    chem_x += chem_vx * time_step
    chem_y += chem_vy * time_step

    # Ion gravity

    ion_ax = -(G * sun_mass * ion_x) / (ion_x ** 2 + ion_y ** 2) ** (3/2)
    ion_ay = -(G * sun_mass * ion_y) / (ion_x ** 2 + ion_y ** 2) ** (3/2)

    ion_vx += ion_ax * time_step
    ion_vy += ion_ay * time_step

    ion_x += ion_vx * time_step
    ion_y += ion_vy * time_step

    # Ion multiple engines gravity

    ion_m_ax = -(G * sun_mass * ion_m_x) / (ion_m_x ** 2 + ion_m_y ** 2) ** (3/2)
    ion_m_ay = -(G * sun_mass * ion_m_y) / (ion_m_x ** 2 + ion_m_y ** 2) ** (3/2)

    ion_m_vx += ion_m_ax * time_step
    ion_m_vy += ion_m_ay * time_step

    ion_m_x += ion_m_vx * time_step
    ion_m_y += ion_m_vy * time_step

    # burn 2

    if current_time == 259:
       chem_vy -= 2640

    # time updates

    current_time += time_step / 86400

    # angle updates

    earth_angle += earth_angular_speed * time_step / 86400
    mars_angle += mars_angular_speed * time_step / 86400
    chem_angle += 2 * math.pi / 365.24
    ion_angle += 2 * math.pi / 365.24
    ion_m_angle += 2 * math.pi / 365.24

    screen.update()
