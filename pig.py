import random
import sys

class Player:
	def __init__(self,name,total=0):
		self.name = name
		self.total = total
	def newTotal(self, newPoint):
		self.total = self.total + newPoint
class KeepingScore:	
	def addtototalscore(self,rolled_value,total=0):
		total = total + rolled_value
		return total		
	def addtotempscore(self,rolled_value,temptotal=0):
		temptotal = temptotal + rolled_value
		return temptotal
class Game:
	def _int_(self,player,total=0):
		self.player = player
		self.total = total
	def Switchplayer(self,name):
		print("Switching players")
		return 2 if name == 1 else 1
	def currentplayer(self,player):
		#.name is accessed from the Player class that is initialized in line 33.
		print("It is currently %s turn" % (player.name))
	def CurrentScore(self, player):
		print("%s, your current score is %s." % \
		(player.name,player.total))
	def GameOver(self,player,win_points):
		score = player.total
		if score >= win_points:
			print("%s has won." % (player.name))
			print("Restart to play again.")
			sys.exit()
if __name__ == '__main__':
	score = KeepingScore()
	game = Game()
	players = { 1: Player('Player 1'),
				2: Player('Player 2') }
	current_player = 1
	addingtempscore = 0

	game.currentplayer(players[current_player])

	while players[current_player].total < 100:
		decision = input("Type r to roll or h to hold and pass on the turn:" + "\n")	
		if decision == "r":
			rolled_value = random.randrange(1, 7)
			print(rolled_value)
			if rolled_value == 1:
				current_player = game.Switchplayer(current_player)
				game.CurrentScore(players[current_player])
				addingtempscore = 0
			else:
				tempscore = score.addtotempscore(rolled_value)
				addingtempscore = tempscore + addingtempscore
				print("Your turn total is: " + str(addingtempscore))
				game.GameOver(players[current_player], 100)
		elif decision == "h":
			totalscore = score.addtototalscore(addingtempscore)
			#each key in the players dictonary has its own total instanced when the newtotal method is called.
			players[current_player].newTotal(totalscore)
			print("You've added " + str(totalscore) + " to your total score")
			current_player = game.Switchplayer(current_player)
			game.CurrentScore(players[current_player])
			addingtempscore = 0
		else:
			print("enter r - to roll or h - to pass")


