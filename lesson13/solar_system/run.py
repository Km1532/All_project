from turtle import *
from random import randint

from solar_system.classes.planet import Planet
from solar_system.classes.asteroid import Asteroid
from solar_system.tools.screen import WIDTH, HEIGHT
from solar_system.dto.planet import PlanetData


def make_window():
    """Make window instance and settings"""
    screen = Screen()
    screen.title('Solar system')
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor('black')
    screen.cv._rootwindow.resizable(False, False)
    screen.onkey(screen.bye, 'Escape')
    screen.listen()
    screen.tracer(0)
    return screen


def make_base_planet():
    """Make base central planet"""
    base_planet = Turtle(shape='circle')
    base_planet.color('yellow')
    base_planet.shapesize(5, 5)
    return base_planet


def make_planets_data():
    """Planet data"""
    earth = PlanetData((1.0, 1.0), 'blue', 150, 0.004)
    moon = PlanetData((0.5, 0.5), 'grey', 25, 0.016)
    saturn = PlanetData((2.0, 2.0), 'orange', 200, 0.001, 'saturn')
    neptune = PlanetData((2.0, 2.0), 'blue', 400, 0.001, 'neptune')
    mars = PlanetData((0.8, 0.8), 'red', 300, 0.0014)
    phobos = PlanetData((0.3, 0.3), 'grey', 40, 0.012)
    deimos = PlanetData((0.2, 0.2), 'white', 25, 0.016)
    stars_data = {
        'earth': earth,
        'moon': moon,
        'saturn': saturn,
        'mars': mars,
        'phobos': phobos,
        'deimos': deimos,
        'neptune': neptune
    }
    return stars_data


def make_planets():
    """Make planets of solar system"""
    planets_data = make_planets_data()
    earth = Planet(planets_data['earth'], sun)
    moon = Planet(planets_data['moon'], earth)
    neptune = Planet(planets_data['neptune'], sun)
    saturn = Planet(planets_data['saturn'], sun)
    mars = Planet(planets_data['mars'], sun)
    phobos = Planet(planets_data['phobos'], mars)
    deimos = Planet(planets_data['deimos'], mars)
    planets = [earth, moon, saturn, mars, phobos, deimos, neptune]
    return planets


def make_belt_around_planet():
    """Make belt around planet"""
    belt = Turtle()
    belt.hideturtle()
    belt.up()
    belt.width(5)
    belt.speed(0)
    belt.color('white')
    return belt


def make_asteroids():
    """Make asteroids belt around solar system"""
    return [Asteroid(sun, randint(400, 600)) for _ in range(500)]


def move_objects(objects):
    """Move stars"""
    for obj in objects:
        if obj.name != 'star':
            star_circle.goto(obj.xcor(), obj.ycor() - 50)
            star_circle.circle(obj.circle_radius)
            star_circle.down()
        obj.move()


def mainloop():
    """Mainloop of Solar system app"""
    while True:
        star_circle.clear()
        move_objects(stars)
        window.update()


if __name__ == '__main__':
    window = make_window()
    sun = make_base_planet()
    stars = make_planets() + make_asteroids()
    star_circle = make_belt_around_planet()
    mainloop()
