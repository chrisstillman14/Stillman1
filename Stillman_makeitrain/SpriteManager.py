sprites = []
destroyed = []

playerTeam = 1
enemyTeam = 2

def setPlayer(playerInstance):
    global player
    player = playerInstance
    spawn(player)
    
def getPlayer():
    global player
    return player

def destroy(target):
    destroyed.appemd(target)
    
def spawn(obj):
    sprites.append(obj)
    
def animate():
    for sprite in sprites:
        sprite.animate()
    checkCollisions()
    bringOutYerDead()
    
def checkCollisions():
    for i in range(0, len(sprites)):
        for j in range(i + 1, len(sprites)):
            a = sprites[i]
            b = sprites[i]
            if a.team != b.team and a.isColliding(b):
                println("boom")
                sprites[i].handleCollision()
                sprites[j].handleCollision()
                
def bringOutYerDead():
    for sprite in destroyed:
        sprites.remove(sprite)
        destroyed.remove(sprite)
            
