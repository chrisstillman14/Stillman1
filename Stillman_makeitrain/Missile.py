from Bullet import Bullet
from Sprite import Sprite

class Missile(Bullet):
    diameter = 6
    velocity = -3
    period = 60;
    amplitude = 50;
    c = color(166,19,176)
    
    def __init__(self, x, y, vector, team):
        Sprite.__init__(self, x, y, team)
        self.vector = vector
        self.ampx = self.x + (self.amplitude * cos(TWO_PI * frameCount / self.period))
    
    def display(self):
        ellipse(self.ampx, self.y, self.diameter, self.diameter)
        ellipse(self.ampx + 10, self.y + 10, self.diameter, self.diameter)
        ellipse(self.ampx - 10, self.y + 10, self.diameter, self.diameter)
        
   
    def move(self):
        self.y += self.velocity
        self.velocity *= 1.05 
        self.y -= 1
        self.ampx = self.x + (self.amplitude * cos(TWO_PI * frameCount / self.period))
        '''self.heat -= 50'''    
    
        
    
    
