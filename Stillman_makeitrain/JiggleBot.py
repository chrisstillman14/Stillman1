import SpriteManager
from Sprite import Sprite
from Armored import Armored
from Shooter import Shooter
class JiggleBot(Armored, Shooter, Sprite):
    
    speed = 4
    diameter = 50
    c = color(255, 75, 50)
        
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.x = constrain(self.y, 0, height)
        
        
