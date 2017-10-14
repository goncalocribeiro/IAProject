# PROJETO IA 2017/2018
# Goncalo Ribeiro 82303
# Andre Mendonca 82304

import copy

# ------------------------------------ GLOBAL VARIABLES ------------------------------------#
already_checked = set()
nodes = set()

# ------------------------------------ AUXILIARES ------------------------------------#

#Auxiliar function to draw a board
#draw_board(<board>)
def draw_board(board):
    draw_line = ""
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line)):
            draw_line += str(line[j]) + " "
        print(draw_line)
        draw_line = ""

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

def neighbors_same_color(position, board):
	positions = []
	posContent = board_position_content(position, board)

	for neighbor in neighbors(position, board):
		neighbor_content = board_position_content(neighbor, board)
		if posContent == neighbor_content:
			positions.append(neighbor)
	return positions 

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
	line = pos_l(pos)
	column = pos_c(pos)
	return board[line][column]

#board_find_groups(<board>) -> [2 valores]
def board_find_groups(board):
	modBoard = copy.deepcopy(board)
	groups = []
	global already_checked
	global nodes

	for line in range(len(modBoard)):
		for column in range(len(modBoard[line])):
			currentPos = make_pos(line, column)

			if board_position_content(currentPos, modBoard) != 0: #ignore the zeros on board
				if currentPos not in already_checked:
					groups.append(connected_colors(currentPos, modBoard))
					nodes = set() #reset nodes from last connected_values search
	return groups

#board_remove_group(<board>, <group>) -> [5 valores]

# ------------------------------------ EXEMPLOS DE CHAMADAS ------------------------------------#

#Tabuleiro 4x5, 3 cores
b0 = [[1,0,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]]
#Tabuleiro 4x5, 2 cores sem solucao
b1 = [[1,2,1,2,1],[2,1,2,1,2],[1,2,1,2,1],[2,1,2,1,2]]
#Tabuleiro 4x5, 3 cores
b2 = [[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]]
#Tabuleiro 10x4, 3 cores sem solucao
b3 = [[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[5,1,1,3],[4,5,1,2]]
#Tabuleiro 10x4, 3 cores
b4 = [[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]
#Tabuleiro 10x4, 5 cores
b5 = [[1,1,5,3],[5,3,5,3],[1,2,5,4],[5,2,1,4],[5,3,5,1],[5,3,4,4],[5,5,2,5],[1,1,3,1],[1,2,1,3],[3,3,5,5]]

print(board_find_groups(b0))
draw_board(b0)