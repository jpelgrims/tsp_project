import pyglet
from pyglet.window import key
from pyglet.gl import *
from tsp_ga import *

window = pyglet.window.Window(fullscreen=True)
platform = pyglet.window.get_platform()
display = platform.get_default_display()    
screen = display.get_default_screen()
screen_width = screen.width
screen_height = screen.height

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q or symbol == key.ESCAPE:
        pyglet.app.exit()

def update(dt):
    window.clear()
    gen_algo.update()
    draw_route(gen_algo.get_best_route())
    draw_information(gen_algo)

def draw_line(x1, y1, x2, y2, thickness):
    glLineWidth(thickness)
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', (x1, y1, x2, y2)))

def draw_square(x, y, size):
    glRectf(x-size/2, y-size/2, x+size/2, y+size/2)

def draw_route(route):
    for i in range(len(route.cities)-1):
        draw_line(route.cities[i][0], route.cities[i][1], route.cities[i+1][0], route.cities[i+1][1], 3)
    for city in route.cities:
        draw_square(city[0], city[1], 12)

def draw_information(gen_algo):
    pyglet.text.Label('Kortste route',
                        font_name='Arial',
                        font_size=20,
                        x=10, y=gen_algo.map_dimensions.height-80).draw()
    pyglet.text.Label('Afstand: ' + str(round(gen_algo.get_best_route().distance, 1)) + ' pixels',
                        font_name='Arial',
                        font_size=32,
                        x=10, y=gen_algo.map_dimensions.height-50).draw()
    pyglet.text.Label('(tot nu toe):',
                        font_name='Arial',
                        font_size=12,
                        x=170, y=gen_algo.map_dimensions.height-80).draw()

population_size = 500
tournament_size = 5
mutation_rate = 0.01
nr_of_cities = 20
map_dimensions = Dimensions(screen_width, screen_height)

gen_algo = GeneticAlgorithm(population_size,
                            mutation_rate,
                            tournament_size,
                            nr_of_cities, 
                            map_dimensions)

pyglet.clock.schedule_interval(update, 0.001)
pyglet.app.run()