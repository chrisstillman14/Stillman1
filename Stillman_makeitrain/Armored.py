import SpriteManager

from Sprite import Sprite

class Armored(Sprite):
    armor = 5
    
    def display(self):
        stroke(100)
        strokeWeight(self.armor)
        fill(255, 75, 50)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
        
    def handleCollision(self):
        self.armor -= .5
        if self.armor < 0:
            SpriteManager.destroy(self)
