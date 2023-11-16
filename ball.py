import turtle
import random

class Balls:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls) -> None:
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = num_balls
        for i in range(num_balls):
            self.xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
            self.ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
            self.vx.append(random.randint(1, 0.01*canvas_width))
            self.vy.append(random.randint(1, 0.01*canvas_height))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        
    def move(self, i):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]
        

    def draw(self, i):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.ball_color[i])
        turtle.fillcolor(self.ball_color[i])
        turtle.goto(self.xpos[i],self.ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

# def draw_circle(color, size, x, y):
#     # draw a circle of radius equals to size at x, y coordinates and paint it with color
#     turtle.penup()
#     turtle.color(color)
#     turtle.fillcolor(color)
#     turtle.goto(x,y)
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(size)
#     turtle.end_fill()
# 
# def move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
#     # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
#     xpos[i] += vx[i]
#     ypos[i] += vy[i]
# 
#     # if the ball hits the side walls, reverse the vx velocity
#     if abs(xpos[i] + vx[i]) > (canvas_width - ball_radius):
#         vx[i] = -vx[i]
# 
#     # if the ball hits the ceiling or the floor, reverse the vy velocity
#     if abs(ypos[i] + vy[i]) > (canvas_height - ball_radius):
#         vy[i] = -vy[i]
# 
# def initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
#     # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
#     for i in range(num_balls):
#         xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
#         ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
#         vx.append(random.randint(1, 0.01*canvas_width))
#         vy.append(random.randint(1, 0.01*canvas_height))
#         ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
# 