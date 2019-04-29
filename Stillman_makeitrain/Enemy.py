import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
from Shooter import Shooter
mark = 0
wait = 500
go = True
class Enemy(Shooter, Sprite):
    
    speed = 8
    diameter = 30
    c = color(255, 75, 50)

    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
            
    
