import platform
from Bullet import Bullet 
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from ScreenSaverBot import ScreenSaverBot
from JiggleBot import JiggleBot
import SpriteManager

mark = 0
wait = 1000
go = True
def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/4, height/2, 1)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Enemy(200,100, 2))
    SpriteManager.spawn(JiggleBot(200, 50, 2 ))
    
                    
def draw():
    global player, sprites
    background(255)   
    SpriteManager.animate()
    global go, mark, wait
    if(millis() - mark > wait):
        go = not go
        mark = millis()
        
    if(go):
        fill(255,0,0)
    else:
        fill(0,255,0)
        
    ellipse (250,250,50,50)
        
        
    
def keyPressed():
    SpriteManager.player.keyDown()   
        
def keyReleased():
    SpriteManager.player.keyUp()
