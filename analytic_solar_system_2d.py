import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

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

mars = turtle.Turtle()
mars.shape("circle")
mars.color("red")
mars.penup()

earth_angle = 0
mars_angle = math.pi / 2#0.773180858633
earth_angular_speed = 2 * math.pi / 364.24
mars_angular_speed = 2 * math.pi / 686.98

x = 149.5978707e9 # 1e9 m = 1 px
y = 0
vx = 0
vy = 29780 + 2940
G = 6.6743e-11
m = 1
sun_mass = 1.989e30

current_time = 0
time_step = 0.1 * 86400

while True:
    earth.goto(149.5978707 * math.cos(earth_angle), 149.5978707 * math.sin(earth_angle))
    mars.goto(227.94 * math.cos(mars_angle), 227.94 * math.sin(mars_angle))
    #ball.goto(x / 1e9, y / 1e9)

    earth.pendown()
    mars.pendown()
    #ball.pendown()

    print("Time (Days):", current_time)

    #Fx = -(G * m * sun_mass * x) / (x ** 2 + y ** 2) ** (3/2)
    #Fy = -(G * m * sun_mass * y) / (x ** 2 + y ** 2) ** (3/2)

    #ax = Fx / m
    #ay = Fy / m

    #vx += ax * time_step
    #vy += ay * time_step

    #x += vx * time_step
    #y += vy * time_step

    current_time += time_step / 86400

    if current_time == 259:
        vy -= 2640

    earth_angle += earth_angular_speed * time_step / 86400
    mars_angle += mars_angular_speed * time_step / 86400

    screen.update()
