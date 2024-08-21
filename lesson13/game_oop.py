from random import random, randint, choice
from turtle import Screen, Turtle


class Window:
    WIDTH = 800
    HEIGHT = 600
    WIDTH_HALF = WIDTH // 2
    HEIGHT_HALF = HEIGHT // 2

    def __init__(self, screen_title: str = 'Window title'):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.setup(self.WIDTH, self.HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.listen()
        self.canvas.tracer(0)


class Sprite(Turtle):
    """Base sprite"""
    def __init__(self, shape_name: str):
        super().__init__(shape=shape_name)
        self.hideturtle()
        self.up()


class Figure(Sprite):
    size = 20

    def __init__(self, figure: str):
        super().__init__(figure)
        self.color(self.generate_color())
        self.goto(self.get_random_position())
        self.showturtle()
        self.delta_x = 0
        self.delta_y = 0

    def move(self, gravity: float):
        self.delta_y -= gravity
        self.goto(self.xcor() + self.delta_x, self.ycor() + self.delta_y)

    @staticmethod
    def generate_color():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        x = randint(-Window.WIDTH_HALF, Window.WIDTH_HALF)
        y = randint(0, Window.HEIGHT)
        return x, y


class Game:
    __directions = -1, 1
    __gravity = 0.1
    __figures_qty = 0

    def __init__(self, figures_qty: int):
        Game.__figures_qty = figures_qty
        self.window = Window()
        self.figures = self.make_figures(figures_qty)

    def run(self):
        for figure in self.figures:
            figure.delta_x = 2 * choice(self.__directions)
            figure.delta_y = 2

        while True:
            for figure in self.figures:
                figure.move(Game.__gravity)
                self.check_border(figure)
            self.window.canvas.update()
            self.check_collision()

    def check_collision(self):
        for i in range(len(self.figures)):
            for j in range(i + 1, len(self.figures)):
                if self.figures[i].distance(self.figures[j]) < 20:
                    self.figures[i].delta_x, self.figures[j].delta_x = self.figures[j].delta_x, self.figures[i].delta_x
                    self.figures[i].delta_y, self.figures[j].delta_y = self.figures[j].delta_y, self.figures[i].delta_y

    def check_border(self, figure):
        x = figure.xcor()
        y = figure.ycor()

        if y < -self.window.HEIGHT_HALF + figure.size // 2:
            figure.sety(-self.window.HEIGHT_HALF + figure.size // 2)
            figure.delta_y = -figure.delta_y

        if x > self.window.WIDTH_HALF - figure.size // 2:
            figure.setx(self.window.WIDTH_HALF - figure.size // 2)
            figure.delta_x = -figure.delta_x
        elif x < -self.window.WIDTH_HALF + figure.size // 2:
            figure.setx(-self.window.WIDTH_HALF + figure.size // 2)
            figure.delta_x = -figure.delta_x

    @staticmethod
    def make_figures(qty: int):
        shapes = ('turtle', 'circle', 'square', 'triangle')
        return [Figure(choice(shapes)) for _ in range(qty)]


if __name__ == '__main__':
    game = Game(figures_qty=100)
    game.run()
