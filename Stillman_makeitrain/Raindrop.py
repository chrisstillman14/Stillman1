import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
from Shooter import Shooter
mark = 0
wait = 500
go = True
class Raindrop(Shooter, Sprite):
    speed = 4
    diameter = 50
    c = color(255, 75, 50)
    

        
    def move(self):
        self.y += self.speed
        if self.y < 0:
            self.speed *= -1
        if self.y > width:
            self.y = 0
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
            
        
