''' 
 abstraction - showing only useful info,hiding the implementation 
 encapsulation - binding of data members and methods, example is class which binds data members
 and methods 
 inheritance - inherit properties from different classes 
 polymosphism - compile time(overloading) run time(overriding) 
'''
import random
class player:
    def __init__(self,name,curPos=0):
        self.name = name
        self.curPos = curPos
    def setPos(self,newPos):
        self.curPos = newPos
class dice:
    def __init__(self,num):
        self.noOfDices = num 
    def rollDice(self):
        import random
        ans = random.randrange(1, self.noOfDices + 1)
        return ans
        
class jumper:
    def __init__(self,startPos,endPos):
        self.spos = startPos
        self.epos = endPos
        if startPos < endPos:
            self.desc = "ladder"
        else:
            self.desc = "snake"
        
class board:
    def __init__(self,size,dice,snakes,ladders,players):
        self.boardSize = size
        self.snakesPosition = snakes
        self.dice = dice
        self.laddersPosition = ladders
        # self.players = players
        self.pq = players
        
        #self.curPos = {} ##  pname:boardPos
    
    def nextTurn(self,player,nextPos):
        if nextPos > self.boardSize:
            self.pq.append(player)
            return False
        elif nextPos == self.boardSize:
            print(player.name,"has won the match--------------")
            return True
        else:
            '''
                 3 cases 
             1. normal cell 
             2. snake bite 
             3. ladder
            '''
            snakeBite = None
            ladderJump = None
            for snake in self.snakesPosition:
                if snake.spos == nextPos:
                    snakeBite = snake 
                    break 
            if snakeBite:
                #self.curPos[player.name] = snakeBite.epos
                player.setPos(snakeBite.epos)
                self.pq.append(player)
                print(player.name,"has been bitten") 
                return False
            for ladder in self.laddersPosition:
                if ladder.spos == nextPos:
                    ladderJump = ladder
                    print(player.name,"has jumped the ladder") 
                    break 
            if ladderJump:
                #self.curPos[player.name] = ladderJump.epos
                player.setPos(ladderJump.epos)
                self.pq.append(player)
                return False
            if not snakeBite and not ladderJump:
                #self.curPos[player.name] = nextPos
                player.setPos(nextPos)
                self.pq.append(player)
                print(player.name,"has changed the position")
                return False
            
    def playgame(self):
        while self.pq:
            currp = self.pq.pop(0)
            currpos = currp.curPos
            diceVal = self.dice.rollDice()
            nextPos  = currpos + diceVal
            self.nextTurn(currp,nextPos)
            '''
            if(self.nextTurn(currp,nextPos)):
                print("MATCH ENDEDNDDDDD")
                return
            else:
                continue'''
    
def getInput():
    print("Enter board size")
    boardSize = int(input())
    # ------- ----------------------#
    print("Enter no of dices")
    noOfDices = int(input())
    diceObj = dice(noOfDices)
    # ------- ----------------------#
    print("Enter no of players")
    noOfPlayers = int(input())
    players = []
    print("Enter name of players")
    for i in range(noOfPlayers):
        name = input()
        playerObj = player(name)
        print(playerObj.name)
        players.append(playerObj)
        
    # ------- ----------------------#
    print("Enter no of snakes")
    noOfSnakes = int(input()) 
    print("Enter snakes starting and ending pos")
    snakes = [] 
    for i in range(noOfSnakes):
        s,e = map(int,input().split())
        snakeObj = jumper(s,e)
        snakes.append(snakeObj)
    # ------- ----------------------#
    print("Enter no of ladders")
    noOfLadders = int(input()) 
    print("Enter ladders starting and ending pos")
    ladders = [] 
    for i in range(noOfLadders):
        s,e = map(int,input().split())
        ladderObj = jumper(s,e)
        ladders.append(ladderObj) 
    gameObj = board(boardSize,diceObj,snakes,ladders,players)
    gameObj.playgame()
    # ------- ----------------------#
getInput()
    
    
        
        
