import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
from PeaShooter import PeaShooter
from Shooter import Shooter
from MissileShooter import MissileShooter
mark = 0
wait = 1000
go = True

class Player(Sprite):
    
    # instance variables
    left = False
    right = False
    up = False
    down = False
    speed = 5
    diameter = 50
    c = color(9, 113, 183)
    
    def handleCollision(self):
        pass
        
    def __init__(self, x, y, team):
        Sprite.__init__(self, x, y, team)
        self.primaryWeapon = MissileShooter(self)
        
    def fire(self, vector = None):
        if vector is None:
            self.primaryWeapon.shoot(PVector(0, -10))
        else: 
            self.primaryWeapon.shoot(vector)
        
    def move(self):
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        self.x = constrain(self.x, self.diameter / 2, width - self.diameter / 2)
        self.y = constrain(self.y, self.diameter / 2, height - self.diameter / 2)

    def keyDown(self):
        if key == 'f' or key == 'F':
            self.fire()
    
        if keyCode == LEFT:
            self.left = True
        if keyCode == RIGHT:
            self.right = True
        if keyCode == UP:
            self.up = True
        if keyCode == DOWN:
            self.down = True
            
    def keyUp(self):
        if keyCode == LEFT:
            self.left = False
        if keyCode == RIGHT:
            self.right = False
        if keyCode == UP:
            self.up = False
        if keyCode == DOWN:
            self.down = False
