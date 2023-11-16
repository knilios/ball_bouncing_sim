import turtle
import ball

class Run_balls:
    def __init__(self):
        self.num_balls = int(input("Number of balls to simulate: "))
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.balls = ball.Balls(self.canvas_width, self.canvas_height, self.ball_radius, self.num_balls)

    def run(self):
        while (True):
            turtle.clear()
            for i in range(self.balls.num_balls):
                self.balls.draw(i)
                self.balls.move(i)
            turtle.update()
        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()


run_balls = Run_balls()
run_balls.run()