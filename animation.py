import turtle as t
import random
import math
import time

# ---------- SETUP SCREEN ----------
screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#1d3557")
screen.title("Love Animation")
screen.tracer(0)  # turn off automatic screen updates

# ---------- SHOW MESSAGE ----------
text = t.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(0, -50)
text.write("I love you Sana ❤️", align="center", font=("Courier New", 30, "bold"))

# ---------- HEART SHAPE ----------
def draw_heart(turtle, size):
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(size)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(size * math.pi / 180)
    turtle.setheading(60)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(size * math.pi / 180)
    turtle.forward(size)
    turtle.end_fill()

# ---------- CREATE HEART OBJECTS ----------
NUM_HEARTS = 3
hearts = []

for _ in range(NUM_HEARTS):
    h = t.Turtle()
    h.hideturtle()
    h.penup()
    h.speed(0)
    h.color("#e63946")
    h.goto(random.randint(-350, 350), random.randint(-300, 200))
    size = random.randint(8, 16)
    vy = random.uniform(0.5, 1.5)
    hearts.append({
        "turtle": h,
        "size": size,
        "vy": vy,
        "phase": random.uniform(0, 2 * math.pi)
    })

# ---------- MAIN LOOP ----------
while True:
    for heart in hearts:
        h = heart["turtle"]
        size = heart["size"]
        vy = heart["vy"]
        phase = heart["phase"]
        
        # Erase previous drawing
        h.clear()
        
        # Update position
        x, y = h.position()
        y += vy
        x += math.sin(time.time() * 2 + phase) * 1  # swaying
        if y > 310:
            y = -310
            x = random.randint(-350, 350)
        h.goto(x, y)
        
        # Draw heart
        h.setheading(0)
        h.begin_fill()
        draw_heart(h, size)
        h.end_fill()
    
    screen.update()
    time.sleep(1 / 60)
