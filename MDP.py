import copy
from random import *

def V6():

	rewardMatrix = ([0,5,-2,10],
				         [0, 5, 0, 15],
						 [-5, 10,  5, 0],
						 [60, 0, 0,  5])

	functionUtil = copy.deepcopy(rewardMatrix)
	directions = copy.deepcopy(rewardMatrix)

	correctMove = .7
	oppositeMove = .2
	noMove = .1

	for horizon in range(0,6):

		cUtil = copy.deepcopy(functionUtil)
		for row in range(0,4):
			for col in range(0,4):
				up = 0
				down = 0
				left = 0
				right = 0
                #calculations:
				#operations for up
				if( (row == 0 and col == 3) or (row == 0 and col == 2) or (row == 0 and col == 1) or (row == 0 and col == 0) ):
					up = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col]) +
						(oppositeMove * functionUtil[row + 1][col]) + (noMove * functionUtil[row][col]) )
				#Bottom
				elif( (row == 3 and col == 3) or (row == 3 and col == 2) or (row == 3 and col == 1) or (row == 3 and col == 0) ):
					up = ( rewardMatrix[row][col] + (correctMove * functionUtil[row - 1][col]) +
						(oppositeMove * functionUtil[row][col]) + (noMove * functionUtil[row][col]) )
				else:
					up = ( rewardMatrix[row][col] + (correctMove * functionUtil[row - 1][col]) +
						(oppositeMove * functionUtil[row + 1][col]) + (noMove * functionUtil[row][col]) )

				#down operation
				if( (row == 3 and col == 3) or (row == 3 and col == 2) or (row == 3 and col == 1) or (row == 3 and col == 0) ):
					down = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col]) +
						(oppositeMove * functionUtil[row - 1][col]) + (noMove * functionUtil[row][col]) )
				#Top
				elif( (row == 0 and col == 3) or (row == 0 and col == 2) or (row == 0 and col == 1) or (row == 0 and col == 0) ):
					down = ( rewardMatrix[row][col] + (correctMove * functionUtil[row + 1][col]) +
						(oppositeMove * functionUtil[row][col]) + (noMove * functionUtil[row][col]))
				else:
					down = ( rewardMatrix[row][col] + (correctMove * functionUtil[row + 1][col]) +
						(oppositeMove * functionUtil[row - 1][col]) + (noMove * functionUtil[row][col]))

				#doublecheck on left side
				if( (row == 3 and col == 0) or (row == 2 and col == 0) or (row == 1 and col == 0) or (row == 0 and col == 0) ):
					left = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col]) +
						(oppositeMove * functionUtil[row][col + 1]) + (noMove * functionUtil[row][col]))
				#right operation 
				elif( (row == 3 and col == 3) or (row == 2 and col == 3) or (row == 1 and col == 3) or (row == 0 and col == 3) ):
					left = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col - 1]) +
						(oppositeMove * functionUtil[row][col]) + (noMove * functionUtil[row][col]))
				else:
					left = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col - 1]) +
						(oppositeMove * functionUtil[row][col + 1]) + (noMove * functionUtil[row][col]))

				#doublecheck on right side
				if( (row == 3 and col == 3) or (row == 2 and col == 3) or (row == 1 and col == 3) or (row == 0 and col == 3) ):
					right = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col]) +
						(oppositeMove * functionUtil[row][col - 1]) + (noMove * functionUtil[row][col]))
				#Left side
				elif( (row == 3 and col == 0) or (row == 2 and col == 0) or (row == 1 and col == 0) or (row == 0 and col == 0) ):
					right = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col + 1]) +
						(oppositeMove * functionUtil[row][col]) + (noMove * functionUtil[row][col]))
				else:
					right = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col + 1]) +
						(oppositeMove * functionUtil[row][col - 1]) + (noMove * functionUtil[row][col]))

			
				vals = {"^": up, "v": down, "<": left, ">": right}
				winner = max(vals.values())
				cUtil[row][col] = winner
				winners = []
				for k,v in vals.items():
					if(v == winner):
						winners.append(k)
				
				directions[row][col] = winners
			
		functionUtil = copy.deepcopy(cUtil)
	
	print()
	print("V^6:")
	for i in range(0,4):
		for j in range(0,4):
			print( round(functionUtil[i][j], 3), end="  ")
		print()

	print()

	print("the V^6 directions:")
	for i in range(0,4):
		for j in range(0,4):
			print( choice(directions[i][j]), end="  ")
		print()

	print()

V6() #call the function

def VCont():


	rewardMatrix = [ [0,5,-2,10],
				     [0,5,0,15],
				     [-5,10,5,0],
				     [60,0,0,5] ]

	functionUtil = copy.deepcopy(rewardMatrix)
	directions = copy.deepcopy(rewardMatrix)

	correctMove = .7
	oppositeMove = .2
	noMove = .1
	discount = .96
	epsilon = .004

	cUtil = copy.deepcopy(functionUtil)

	while( True ): #this is different than before, now we need to loop continously until we hit the ideal tolerance
	
		delta = 0

		for row in range(0,4):

			for col in range(0,4):

				up = 0
				down = 0
				left = 0
				right = 0

				if( (row == 0 and col == 3) or (row == 0 and col == 2) or (row == 0 and col == 1) or (row == 0 and col == 0) ):
					up = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col]) +
						(oppositeMove * functionUtil[row + 1][col]) + (noMove * functionUtil[row][col]) )
				elif( (row == 3 and col == 3) or (row == 3 and col == 2) or (row == 3 and col == 1) or (row == 3 and col == 0) ):
					up = ( rewardMatrix[row][col] + (correctMove * functionUtil[row - 1][col]) +
						(oppositeMove * functionUtil[row][col]) + (noMove * functionUtil[row][col]) )
				else:
					up = ( rewardMatrix[row][col] + (correctMove * functionUtil[row - 1][col]) +
						(oppositeMove * functionUtil[row + 1][col]) + (noMove * functionUtil[row][col]) )

				if( (row == 3 and col == 3) or (row == 3 and col == 2) or (row == 3 and col == 1) or (row == 3 and col == 0) ):
					down = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col]) +
						(oppositeMove * functionUtil[row - 1][col]) + (noMove * functionUtil[row][col]) )
				elif( (row == 0 and col == 3) or (row == 0 and col == 2) or (row == 0 and col == 1) or (row == 0 and col == 0) ):
					down = ( rewardMatrix[row][col] + (correctMove * functionUtil[row + 1][col]) +
						(oppositeMove * functionUtil[row][col]) + (noMove * functionUtil[row][col]))
				else:
					down = ( rewardMatrix[row][col] + (correctMove * functionUtil[row + 1][col]) +
						(oppositeMove * functionUtil[row - 1][col]) + (noMove * functionUtil[row][col]))

				if( (row == 3 and col == 0) or (row == 2 and col == 0) or (row == 1 and col == 0) or (row == 0 and col == 0) ):
					left = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col]) +
						(oppositeMove * functionUtil[row][col + 1]) + (noMove * functionUtil[row][col]))
				elif( (row == 3 and col == 3) or (row == 2 and col == 3) or (row == 1 and col == 3) or (row == 0 and col == 3) ):
					left = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col - 1]) +
						(oppositeMove * functionUtil[row][col]) + (noMove * functionUtil[row][col]))
				else:
					left = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col - 1]) +
						(oppositeMove * functionUtil[row][col + 1]) + (noMove * functionUtil[row][col]))

				if( (row == 3 and col == 3) or (row == 2 and col == 3) or (row == 1 and col == 3) or (row == 0 and col == 3) ):
					right = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col]) +
						(oppositeMove * functionUtil[row][col - 1]) + (noMove * functionUtil[row][col]))
				elif( (row == 3 and col == 0) or (row == 2 and col == 0) or (row == 1 and col == 0) or (row == 0 and col == 0) ):
					right = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col + 1]) +
						(oppositeMove * functionUtil[row][col]) + (noMove * functionUtil[row][col]))
				else:
					right = ( rewardMatrix[row][col] + (correctMove * functionUtil[row][col + 1]) +
						(oppositeMove * functionUtil[row][col - 1]) + (noMove * functionUtil[row][col]))

				vals = {"^": up, "v": down, "<": left, ">": right}
				winner = max(vals.values())
				cUtil[row][col] = winner * discount
				winners = []
				for k,v in vals.items():
					if(v == winner):
						winners.append(k)
				directions[row][col] = winners

				delta = max(delta, abs(cUtil[row][col] - functionUtil[row][col]))

		functionUtil = copy.deepcopy(cUtil)
		
		if(delta < (epsilon * (1 - discount) / discount)):	
		
			print("V*:")
			for i in range(0,4):
				for j in range(0,4):
					print( round(1.04165 * functionUtil[i][j], 3), end="  ")
				print()

			print()

			print("The V* directions:")
			for i in range(0,4):
				for j in range(0,4):
					print( choice(directions[i][j]), end="  ")
				print()

			print()
			
			return
VCont()