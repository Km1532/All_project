import os
from pathlib import Path
from random import random, randint, choice
from turtle import Screen, Turtle
from Turtle_game import picture

# PATH_TO_PIC = Path(picture.__file__).parent.absolute()


class Window:
    WIDTH = 800
    HEIGHT = 600
    WIDTH_HALF = WIDTH // 2
    HEIGHT_HALF = HEIGHT // 2

    def __init__(self, screen_title: str = 'Turtle go go go.... '):
        self.canvas = Screen()
        self.canvas.title(screen_title)
        self.canvas.setup(self.WIDTH, self.HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.bgcolor('black')
        # self.canvas.bgpic(os.path.join(PATH_TO_PIC, 'sea.png'))
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

    def move(self, speed: float):
        self.goto(self.xcor() - self.delta_x, self.ycor() + self.delta_y)

    @staticmethod
    def generate_color():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        x = randint(Window.WIDTH_HALF, 10 * Window.HEIGHT)
        y = randint(-Window.HEIGHT + 400, Window.HEIGHT - 400)
        return x, y


class Game:
    __directions = -1, 3
    __speed = 1
    __figures_qty = 0

    def __init__(self, figures_qty: int):
        Game.__figures_qty = figures_qty
        self.window = Window()
        self.figures = self.make_figures(figures_qty)

    def run(self):
        for figure in self.figures:
            figure.delta_x = 2  # * choice(self.__directions)
            figure.delta_y = 0  # * choice(self.__directions)

        while True:
            for figure in self.figures:
                figure.move(Game.__speed)
                self.check_border(figure)
            self.window.canvas.update()

    def check_border(self, figure):
        x = figure.xcor()
        if x < -self.window.WIDTH_HALF + figure.size // 2:
            figure.goto(Figure.get_random_position())

    @staticmethod
    def make_figures(qty: int):
        shapes = ('circle', 'square')
        return [Figure(choice(shapes)) for _ in range(qty)]


if __name__ == '__main__':
    game = Game(figures_qty=100)
    game.run()
