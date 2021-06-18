from abc import ABC

class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, line):
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

class RasterRenderer(Renderer):
    def render_cirle(self, radius):
        print(f'Drawing pixels for a circle with radius {radius}')

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self):
        pass

    def resize(self):
        pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)
    
    def resize(self, factor):
        self.radius *= factor

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()