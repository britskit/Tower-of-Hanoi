from Stack import Stack
import Hanoi as h


# intialising poles
a, b, c = Stack(), Stack(), Stack()
poles = [a, b, c]

# initialising moves stack
moves = Stack()

print '''
 _____ _____ _ _ _ _____ _____   
|_   _|     | | | |   __| __  | 
  | | |  |  | | | |   __|    -| 
  |_| |_____|_____|_____|__|__| 
          _____ _____                   
         |     |   __|                  
         |  |  |   __|                  
         |_____|__|                     
 _____ _____ _____ _____ _____  
|  |  |  _  |   | |     |     | 
|     |     | | | |  |  |-   -| 
|__|__|__|__|_|___|_____|_____| 
                                 
\033[1mVersion 1.1\n\033[0m
* Auto solve from any position with backtracking
* Supports 3 to 10 discs

\033[1mHow to play:\n\033[0m
Move all the discs from the first pole to the third one by one.
Rule: a larger disc cannot be placed on top of a smaller disc.\n
Coded by Avery
_______________________________________________________________________'''

# populating stack with discs
# only caters to 2 and 4 atm because of the layout 
# but algo will work for any number of discs
disc = h.prompt_start("Number of discs (min: 3, max: 10): ")
for i in range(disc, 0, -1):
	a.push(i)

while 1: 
	h.view_all(disc, a, b, c)
	x, y = h.prompt("Type \"0 0\" to auto-solve. \nDisc to move (eg type \"1 2\" to move disc from pole 1 to pole 2):\n")

	# user entered auto-solve
	if x == 0 and y == 0:
		h.view_all(disc, a, b, c)
		h.backtrack(disc, poles, moves)
		break

	# user entered pole numbers to move
	else:
		# if move is valid
		if h.move_disc(poles[x - 1], poles[y - 1]) == 1:
			moves.push([x, y])
			h.view_all(disc, a, b, c)

			if h.is_solved(poles, disc):
				print "\n ##### SOLVED ##### \n"
				exit()

		else:
			print "\nInvalid move."
			h.time.sleep(.5)
			
		continue
    