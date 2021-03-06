# Goncalo Ribeiro 82303
# Andre Mendonca 82304
# AL030
import copy
from search import *

# ------------------------------------ GLOBAL VARIABLES ------------------------------------#
already_checked = set()
nodes = set()

# ------------------------------------ AUXILIARES ------------------------------------#

#Auxiliar function to draw a board like a matrix
#draw_board(<board>)
def draw_board(board):
    draw_line = ""
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line)):
            draw_line += str(line[j]) + " "
        print(draw_line)
        draw_line = ""

#returns True is pos2 is an adjacent position to pos1, False in other case
def is_adjacent(pos1, pos2):
	pos1Line = pos_l(pos1)
	pos1Column = pos_c(pos1)
	pos2Line = pos_l(pos2)
	pos2Column = pos_c(pos2)

	if(pos1Line == pos2Line):
		if((pos1Column == pos2Column-1) or (pos1Column == pos2Column+1)):
			return True
	elif(pos1Column == pos2Column):
		if((pos1Line == pos2Line-1) or (pos1Line == pos2Line+1)):
			return True
	return False

#returns a list of all adjacent positions to position
def neighbors(position, board):
	boardLSize = board_l(board)
	boardCSize = board_c(board)

	posLine = pos_l(position)
	posColumn = pos_c(position)

	neighbors = []

	for l in range(0,boardLSize):
		for c in range(0,boardCSize): 
			currentPos = make_pos(l,c)
			if(is_adjacent(position,currentPos)):
				neighbors.append(currentPos)
	return neighbors

#returns a list of all adjacent positions to position that has the same color(content)
def neighbors_same_color(position, board):
	positions = []
	posContent = board_position_content(position, board)

	for neighbor in neighbors(position, board):
		neighbor_content = board_position_content(neighbor, board)
		if posContent == neighbor_content:
			positions.append(neighbor)
	return positions 

#returns the group of positions connected to position with the same color
def connected_colors(position, board):
	global already_checked
	already_checked.add(position)
	global nodes

	neighbors = neighbors_same_color(position, board)

	if (len(neighbors) != 0):
		for neighbor in neighbors:
			nodes.add(neighbor)
			if neighbor not in already_checked:
				connected_colors(neighbor, board)
	else:
		nodes.add(position)
	return list(nodes)

def vertical_compaction(board):
	count = 0

	for column in range(board_c(board)):
		for row in range(board_l(board)-1, -1, -1):
			position = make_pos(row, column)
			position_content = board_position_content(position, board)

			if position_content == 0:
				count += 1
				for index in range (row-1, -1, -1):
					index_position = make_pos(index, column)
					index_position_content = board_position_content(index_position, board)

					if index_position_content == 0:
						count += 1
					else:
						board[index+count][column] = index_position_content
						board[index][column] = 0
				count = 0
				break
	return board


def horizontal_compaction(board):
	row_init = board_l(board)-1
	column_init = board_c(board)-1
	count = 1

	column = 0

	while column <= column_init:
		position = make_pos(row_init, column)
		posCont = board_position_content(position, board)

		if posCont == 0:
			i_column = column +1
			while i_column <= column_init:
				pos = make_pos(row_init, i_column)
				posC = board_position_content(pos, board)

				if posC != 0:
					i_row = row_init
					while i_row >= 0:
						pos_aux = make_pos(i_row, i_column)
						pos_auxC = board_position_content(pos_aux, board)

						if pos_auxC != 0:
							board[i_row][i_column-count] = pos_auxC
							board[i_row][i_column] = 0
						i_row -= 1
				else:
					count += 1
				i_column += 1
			count = 1
		column += 1
	return board

# ------------------------------------ TIPOS ------------------------------------#

# TAI color
# sem cor = 0
# com cor > 0
def get_no_color():
    return 0
def no_color(c):
    return c==0
def color(c):
    return c > 0

#TAI pos
#Tuplo (l, c)
def make_pos(l, c):
    return (l, c)
def pos_l(pos):
    return pos[0]
def pos_c(pos):
    return pos[1]

#TAI board
def board_c(board):
	return len(board[0])

def board_l(board):
	return len(board)

def board_position_content(pos, board):
	row = pos_l(pos)
	column = pos_c(pos)
	return board[row][column]
#def board_column_content(row, column, board):


#board_find_groups(<board>) -> [2 valores]
def board_find_groups(board):
	groups = []
	global already_checked
	global nodes

	for row in range(len(board)):
		for column in range(len(board[row])):
			currentPos = make_pos(row, column)

			if board_position_content(currentPos, board) != 0: #ignore the zeros on board
				if currentPos not in already_checked:
					groups.append(connected_colors(currentPos, board))
					nodes = set() #reset nodes from last connected_values search
	return groups

#board_remove_group(<board>, <group>) -> [5 valores]
def board_remove_group(board, group):
	modBoard = copy.deepcopy(board)
	for pos in group:
		row = pos_l(pos)
		column = pos_c(pos)
		modBoard[row][column] = 0

	#return modBoard
	#return vertical_compaction(modBoard)
	return horizontal_compaction(vertical_compaction(modBoard))

#remove every single group from groups
def clean_single_lists(groups):
	to_delete = []
	for index in range(len(groups)):
		if len(groups[index]) == 1:
			to_delete.append(groups[index])

	for lst in to_delete:
		groups.remove(lst)

	return groups

class sg_state:
	def __init__(self, board):
		self.board = board

	#necessary for A* and other informed searches
	def __lt__(self, state):
		return self.board < state.board

class same_game(Problem):
	"""Models a Same Game problem as a satisfaction problem.
	   A solution cannot have pieces left on the board."""

	def __init__(self, board):
		self.board = board
		self.initial = sg_state(board)
		self.goal = sg_state([]) #the goal is to get an empty list from actions

	def actions(self, state):
		#Returns a list of groups with more than 2 elements
		return clean_single_lists(board_find_groups(state.board))

	def result (self, state, action):
		#Returns a new state (call board_remove_group)
		return sg_state(board_remove_group(state.board, action))

	def goal_test(self, state):
		#Returns True if state is the goal state (when board_find_groups returns an empty list)
		return board_find_groups(state.board) == self.goal.board

	def h(self, node):
		"""Needed for informed search
		Heuristic method to help A* and Gridy search
		return False"""
