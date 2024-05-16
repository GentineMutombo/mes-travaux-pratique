class Forme:
    def __init__(self,largeur,longueur):
        self.largeur=largeur
        self.longueur=longueur
class Triangle(Forme):
    def aire(self):
        return (self.largeur*self.longueur)/2
    
class Rectangle(Forme):
    def aire(self):
        return self.largeur*self.longueur
    
rectangle=Rectangle(100,200)
triangle=Triangle(100,150)

print(rectangle.aire())
print(triangle.aire())

