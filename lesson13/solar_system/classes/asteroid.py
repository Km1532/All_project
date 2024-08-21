from random import random
from math import sin, cos

from solar_system.classes.planet import Planet
from solar_system.dto.planet import PlanetData


class Asteroid(Planet):
    start_angle = 0.001
    increase_start_angle = 0.012421

    def __init__(self, star, radius):
        self.obj = PlanetData((0.1, 0.1), self.generate_color(), radius, self.increase_start_angle)
        Planet.__init__(self, self.obj, star)
        self.angle += self.start_angle
        Asteroid.start_angle += self.increase_start_angle

    def move(self):
        """Move asteroids elipse"""
        # super(Asteroid, self).move()
        # print(self.__class__)
        self.x = self.radius * 2 * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle

    @staticmethod
    def generate_color():
        return random(), random(), random()
