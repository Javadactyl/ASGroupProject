import time
class GameStats():
    # Function that is run initialy setting an mount of lives and cash
    def __init__(self):
        self.health = 5
        self.cash = 100
        self.gameMode = 1
        self.currentTime = 0
        self.startTime = time.time()

    def gameMode(self):
        while True:
            self.gameMode=int(input("Set gamemode to 1 or 2"))
            if self.gameMode!=2 or self.gameMode!=1:
                print("Gamemode must be set to 1 or 2")
                continue
            if self.gameMode == 1:
                self.setHealth(5)
                self.setCash(100)
            else:
                self.setHealth(100)
                self.setCash(300000)
            return self.gameMode
            
    def getCash(self):
        return self.cash
    
    def setCash(self, newCash):
        self.cash = newCash
        
    def getHealth(self):
        return self.health
    
    def setHealth(self, newHealth):
        self.health = newHealth
        
<<<<<<< HEAD
    def CurrentTime():
        CurrentTime=(time.time())
        return CurrentTime
#ALL BELOW NEED TO BE IN A DEBUGGING FUNCTION IN FUTURE
=======
    def currentTime():
        self.currentTime=time.time()-self.startTime
        return currentTime

>>>>>>> 6c3bea53d8d719b2a9ce87c7db983d7b9142092d

GameStats = GameStats()

print(GameStats.getCash())

GameStats.setCash(300000)
print(GameStats.getCash())

print(GameStats.getHealth())

GameStats.setHealth(100)
print(GameStats.getHealth())
