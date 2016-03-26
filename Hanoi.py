from Stack import Stack
import time
import os


def move_disc(a, b):
	# disallow move from empty pole
	if a.peek() == None:
		return 0

	# allow move to empty pole
	elif b.peek() == None:
		b.push(a.pop())
		return 1

	# disallow larger disc on top of smaller disc
	elif a.peek() > b.peek():
		return 0

	# all other valid moves
	else:
		b.push(a.pop())
		return 1


def view_all(n, a, b, c):
	# delay in seconds
	time.sleep(.025)		

	''' 
	Please change accordingly: 
	'''

	# clear terminal
	os.system("clear") # for mac/linux
	# os.system("cls") # for windows

	'''
	Using this as reference: 

	1:     |        |        |
	2:    ###       |        |
	3:   #####      |        |
	4:  #######     |        |
	5:  -------  -------  -------

	'''
	# row 1
	print "\n", (" " * (n + 1) + "|" + " " * (n + 1)) * 3

	# row 2 to 4
	for i in range(n - 1, -1, -1):
		print "",

		# if there are no discs (has a comma at the end)
		if a.peekAt(i) == None:
			print " " * n + "|" + " " * (n + 1),

		# if there are discs (has a comma at the end)
		else:
			print " " * (n - a.peekAt(i)) + "#" * a.peekAt(i) * 2 + "#" + " " * ((n + 1) - a.peekAt(i)),

		# if there are no discs (has a comma at the end)
		if b.peekAt(i) == None:
			print " " * n + "|" + " " * (n + 1),

		# if there are discs (has a comma at the end)
		else:
			print " " * (n - b.peekAt(i)) + "#" * b.peekAt(i) * 2 + "#" + " " * ((n + 1) - b.peekAt(i)),

		# if there are no discs (has no comma at the end)
		if c.peekAt(i) == None:
			print " " * n + "|" + " " * (n + 1)

		# if there are discs (has no comma at the end)
		else:
			print " " * (n - c.peekAt(i)) + "#" * c.peekAt(i) * 2 + "#" + " " * ((n + 1) - c.peekAt(i))

	# row 5 (base)
	print (" " + "-" * n * 2 + "- ") * 3, "\n"


def solve(n, a, b, c, p, d):
	'''

	n = number of discs (for the algorithm)
	a = first pole
	b = middle pole
	c = last pole 
	p = list of poles in proper order (for printing)
	d = number of discs (for printing)

	'''

	if n == 1:
		moved = move_disc(a, c)

		# if move was successful
		if  moved == 1:
			view_all(d, p[0], p[1], p[2])
		
	else:
		solve(n - 1, a, c, b, p, d)
		solve(1, a, b, c, p, d)
		solve(n - 1, b, a, c, p, d)

	# validating result
	return is_solved(p, d)


def prompt(msg):
	while True:
		var = raw_input("\n%s" % (msg))

		# make sure that the user typed 2 values
		try:
			a, b = var.split(" ")

			# make sure the inputs are valid ints
			try: 
				a, b = int(a), int(b)
				if a < 0 or b < 0 or a > 3 or b > 3:
					print "\nInvalid poles."
					continue
				else:
					break
			except:
				print "\nInvalid format."
		except:
			print "\nInvalid format."

	return a, b


def prompt_start(msg):
	while True:
		var = raw_input("\n%s" % (msg))

		# make sure that the user typed 2 values
		try:
			a = int(var)

			if a < 3 or a > 10:
				print "\nMin: 3, Max: 10."
				continue
			else:
				break
		except:
			print "\nInvalid format."

	return a


def backtrack(disc, poles, moves):
	# save current state 
	saved = save_poles(poles)

	# try to solve
	solved = solve(disc, poles[0], poles[1], poles[2], poles, disc)

	# if unable to solve
	if solved == 0:
		print "\n ##### UNABLE TO SOLVE. BACKTRACKING... ##### \n"
		time.sleep(1)

		# go back one step
		prev_move = moves.pop()
		move_disc(saved[prev_move[1] - 1], saved[prev_move[0] - 1])
		
		# recursive call
		backtrack(disc, saved, moves)

	# solved
	elif solved == 1:	
		print "\n ##### SOLVED ##### \n"


def save_poles(poles):
	# duplicating poles
	a, b, c = Stack(), Stack(), Stack()

	a.copyFrom(poles[0])
	b.copyFrom(poles[1])
	c.copyFrom(poles[2])
	
	saved = [a, b, c]
	
	return saved


def is_solved(p, d):
	# validating result
	if p[0].size() == 0 and p[1].size() == 0 and p[2].size() == d:
		return 1
	else:
		return 0








