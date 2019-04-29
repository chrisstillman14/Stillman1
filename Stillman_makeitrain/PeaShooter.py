from Pea import Pea
import SpriteManager

class PeaShooter:
    wait = 100
    mark = 0
    cooldown = True
    
    def __init__(self, handler):
        self.handler = handler
        
    def shoot(self, vector):
        if self.cooldown:
            pea = Pea(self.handler.x, self.handler.y, vector, self.handler.team)
            SpriteManager.spawn(pea)
            self.cooldown = False
            
        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
