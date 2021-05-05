
from package import board
from package import player

if __name__ == "__main__":

	p1 = player.Player('Lalit','X')
	p2 = player.Player('Bhavesh','O')

	b = board.Board()

	isPlayed=""
	print(" ######### Welcome to the TicTacToe game ##########")
	b.display()

	while True:

		if isPlayed=='p1':
			p=p2
			isPlayed='p2'
		else:
			p=p1
			isPlayed='p1'


		b.flipPlayer(p.getPlayerName(),p.getPlayerChar())

		b.playerMove(p.getPlayerChar())

		b.display()

		if(b.isWinner(p.getPlayerChar())):
			print(f" Congrat {p.getPlayerName()}! You won...")
			break

		if(b.isTie(p.getPlayerChar())):
			print(f" Game tied..")
			break


	