import platform
from Bullet import Bullet 
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from Armored import Armored
from JiggleBot import JiggleBot
from PeaShooter import PeaShooter
import SpriteManager

mark = 0
wait = 1000
go = True


def setup():
    print "Built with Processing Python version " + platform.python_version()
    global player, sprites, img
    img = loadImage("galax.jpg")
    size(1000, 1000)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/4, height/2, 1)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Enemy(250,200, 2))
    SpriteManager.spawn(Enemy(500,200, 2))
    SpriteManager.spawn(Enemy(750,200, 2))
    SpriteManager.spawn(Raindrop(62.5, 25, 2))
    SpriteManager.spawn(Raindrop(937.5, 25, 2))

    SpriteManager.spawn(Armored(125, 100, 2))
    SpriteManager.spawn(Armored(250, 100, 2))
    SpriteManager.spawn(Armored(375, 100, 2))
    SpriteManager.spawn(Armored(500, 100, 2))
    SpriteManager.spawn(Armored(625, 100, 2))
    SpriteManager.spawn(Armored(750, 100, 2))
    SpriteManager.spawn(Armored(875, 100, 2))
    
                    
def draw():
    global player, sprites, img
    background(img)  
    SpriteManager.animate()
    
    
    
def keyPressed():
    SpriteManager.player.keyDown()   
        
def keyReleased():
    SpriteManager.player.keyUp()
