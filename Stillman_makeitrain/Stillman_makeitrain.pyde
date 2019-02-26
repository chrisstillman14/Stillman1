import platform
from Bullet import Bullet 
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, 1)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Enemy(200,100, 2))
                    
def draw():
    global player, sprites
    background(255)   
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()   
        
def keyReleased():
    SpriteManager.player.keyUp()
