# PROJETO IA 2017/2018
# Goncalo Ribeiro 82303
# Andre Mendonca 82304

# ------------------------------------ AUXILIARES ------------------------------------#

#Auxiliar function to draw a board
#draw_board(<board>)
def draw_board(board):
    draw_line = ""
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line)):
            draw_line += str(line[j]) + " "
        print draw_line
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

def adjacent_positions(pos, board):
	boardLSize = board_l(board)
	boardCSize = board_c(board)

	posLine = pos_l(pos)
	posColumn = pos_c(pos)

	adjacentPositions = []

	for l in range(0,boardLSize):
		for c in range(0,boardCSize): 
			currentPos = make_pos(l,c)
			if(is_adjacent(pos,currentPos)):
				adjacentPositions.append(currentPos)
	return adjacentPositions

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

#TAI group
#Lista [(l,c),(l,c),(l,c),...]

#TAI board
def board_c(board):
	return len(board[0])

def board_l(board):
	return len(board)


# ------------------------------------ OPERACOES ------------------------------------#

#board_find_groups(<board>) -> [2 valores]
def board_find_groups(board):
    groups = []
    boardCSize = board_c(board)
    boardLSize = board_l(board)

    for l in range(0, boardLSize):
        for c in range(0, boardCSize):
            g = []
            posCont = board[l][c] #conteudo da posicao

            if(color(posCont)): #posicao tem cor
            	currentPos = make_pos(l,c)
                adjacentPositions = adjacent_positions(currentPos, board) #posicoes adjacentes a atual
                g.append(currentPos)
                
                for i in range(len(adjacentPositions)):
                    adjPos = adjacentPositions[i] #posicao adjacente a posicao que estamos a verificar
                    adjL = pos_l(adjPos) #linha da posicao adjacente
                    adjC = pos_c(adjPos) #coluna da posicao adjacente
                    adjCont = board[adjL][adjC] #conteudo da posicao adjacente

                    if (posCont == adjCont):
                        g.append(adjPos)
            groups.append(g)
    print "GRUPOS:\n" + str(groups)
#board_remove_group(<board>, <group>) -> [5 valores]

# ------------------------------------ EXEMPLOS DE CHAMADAS ------------------------------------#
draw_board([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])
board_find_groups([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])
#print adjacent_positions((2,2),[[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])
