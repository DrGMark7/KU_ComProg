import math

class Cylinder:
    def __init__(self,radius,height) -> None:
        self.radius = radius
        self.height = height

    def __str__(self) -> str:
        return f"Radius: {self.radius :.3f}, Height: {self.height:.3f}"

    def get_radius(self):
        return self.radius
    
    def get_height(self):
        return self.height
    
    def set_radius(self,new_radius):
        self.radius = new_radius

    def set_height(self,new_height):
        self.height = new_height

    def get_base_area(self):
        return (math.pi*self.radius**2)
    
    def get_volume(self):
        return math.pi*(self.radius**2)*self.height