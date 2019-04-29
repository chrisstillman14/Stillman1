import SpriteManager
from Missile import Missile

class MissileShooter:
    
    mark = 0
    wait = 300
    cooldown = True
    
    def __init__(self, handler):
        self.handler = handler
        
            
    def shoot(self, vector):
        if self.cooldown:
            missile = Missile(self.handler.x, self.handler.y, vector, self.handler.team)
            SpriteManager.spawn(missile)
            self.cooldown = False
            
        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
            

            
