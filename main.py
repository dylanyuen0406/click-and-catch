import turtle
import time
import random


class Shape:

    def __init__(self, x, y, shape, color):
        self.shape = turtle.Turtle()
        self.shape.penup()
        self.shape.hideturtle()
        self.shape.speed(0)
        self.shape.goto(x, y)
        self.shape.color(color)
        self.shape.shape(shape)
        self.shape.shapesize(2, 2)

    def move(self):
        self.shape.sety(self.shape.ycor() - 20)

    def hide(self):
        self.shape.hideturtle()

    def show(self):
        self.shape.showturtle()


class Text:

    def __init__(self, x, y, text):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.goto(x, y)
        self.pen.color("black")
        self.write_text(text)

    def write_text(self, text):
        self.pen.clear()
        self.pen.write(text, align="center", font=("Arial", 16, "normal"))


class Game:

    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor("white")
        self.win.title("Catch The Circles!")
        self.win.tracer(0)

        self.shapes = []
        self.score = 0
        self.duration = 45
        self.start_time = time.time()
        self.score_text = Text(-200, 250, f"Score: {self.score}")
        self.timer_text = Text(-200, 250, f"Time: {self.duration}")
    def create_shape(self):
        x = random.randint(-250, 250)
        y = 250
        shape = random.choice(["circle", "square", "triangle"])
        color = random.choice(["red", "blue", "green", "yellow", "purple"])
        new_shape = Shape(x, y, shape, color)
        new_shape.show()
        self.shapes.append(new_shape)

    def move_shapes(self):
        for shape in self.shapes:
            shape.move()

            if shape.shape.ycor() < -250:
                self.shapes.remove(shape)
                shape.hide()
    def on_shape_click(self, x, y):
        for shape in self.shapes:
            if shape.shape.distance(x, y) < 40 and shape.shape.shape() == "circle":
                self.shapes.remove(shape)
                shape.hide()
                self.score += 1

            elif shape.shape.distance(x, y) < 40 and shape.shape.shape() != "circle":
                self.shapes.remove(shape)
                shape.hide()
                self.score -= 1

            self.score_text.write_text(f"Score:{self.score}")

    def update_timer(self):
        time_passed = int(time.time() - self.start_time)
        time_left = max(0, self.duration - time_passed)
        self.timer_text.write_text(f"Time: {time_left}")
        return time_left > 0

    def start(self):
        self.win.listen()
        self.win.onclick(self.on_shape_click)

        while self.update_timer:
            self.win.update()
            self.create_shape()
            self.move_shapes()
            time.sleep(0.1)

        self.win.textinput("Game over!", f"Highest Score: {self.score}")



if __name__ == "__main__":
    game = Game()
    game.start()
