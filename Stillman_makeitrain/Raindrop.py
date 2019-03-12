import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
mark = 0
wait = 1000
go = True
class Raindrop(Sprite):
    speed = 8
    diameter = 50
    c = color(0,0,255)
    

        
    def move(self):
        self.y += self.speed
        if self.y < 0:
            self.speed *= -1
        if self.y > width:
            self.y = 0
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
            
    def aim(self, target) :
        xcomp = target.x - self.x
        ycomp = target.y - self.y
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xVec = xcomp/d
        yVec = ycomp/d
        magnitude = 7
        return PVector(xVec * magnitude,yVec * magnitude)
    
    def fire(self, vector) :
         
         global go, mark, wait
         if(millis() - mark > wait):
            go = not go
            mark = millis()
        
         if(go):
            go = False
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
        
