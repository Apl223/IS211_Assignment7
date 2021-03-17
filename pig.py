import random
import sys
import time


class Player:
    def __init__(self, name, total=0):
        self.name = name
        self.total = total

    def newTotal(self, newPoint):
        self.total = self.total + newPoint

    def decision(self):
        roll = input("Would you like to roll? r = roll, h = pass" + "\n")
        return roll

class Dice:
    def __init__(self, roll=0):
        self.roll =  roll

    def newRoll(self, seed): 
        random.seed(seed)
        self.roll = random.randrange(1, 7)
        return self.roll

class Game:
    def __int__(self, current_player, total=0):
        self.player = current_player
        self.total = total

    def turnScore(self, newPoint):
        self.total = self.total + newPoint
        return self.total

    def totalScoreCheck(self, player, win_ponts):
        score = player.total + self.total
        if score >= win_ponts:
            player.total = score
            print("%s has won." % (player.name))
            print('Your final score is ', player.total)
            self.GameOver()

    def Switch(self, current_player):
        self.total = 0
        print('Switching turns.')
        return 2 if current_player == 1 else 1

    def statusMessage(self, player, new_roll):
        print("%s rolled a %s. Score for this turn is %s and player's total score is %s" % \
        (player.name, new_roll, self.total, player.total ))

    def CurrentScore(self, player):
        print("%s, your current score is %s." % \
        (player.name,player.total))

    def GameOver(self):
        print("Restart to play again.")
        sys.exit()

if __name__ == '__main__':

    seed = random.seed(0)
    dice = Dice(seed)
    game = Game()
    players = { 1: Player('Player 1'),
                2: Player('Player 2')}

    current_player = 1
    game.total = 0
    game.CurrentScore(players[current_player])

    while players[current_player].total < 100 :
        roll = players[current_player].decision()

        if roll == 'r':
            new_roll = dice.newRoll(seed)

            if new_roll == 1:
                game.total = 0
                print("You have rolled a 1")
                current_player = game.Switch(current_player)
                game.CurrentScore(players[current_player])
            else:
                game.total = game.turnScore(new_roll)
                game.statusMessage(players[current_player],new_roll)
                game.totalScoreCheck(players[current_player], 100)

        elif roll == 'h':
            print(players[current_player].name, " adds ", game.total, " points to his total of ", players[current_player].total)
            players[current_player].newTotal(game.total)
            current_player = game.Switch(current_player)
            game.CurrentScore(players[current_player])

        else:
            print("enter r - to roll or h - to pass")

        seed = time.time()