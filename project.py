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

def adjacent_position(pos):
	#return adjacent positions of pos


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


# ------------------------------------ OPERACOES ------------------------------------#

#board_find_groups(<board>) -> [2 valores]
def board_find_groups(board):
    groups = []
    for i in range(len(board)):
        line = board[i]
        for j in range(len(line)):
            positionCont = line[j] #conteudo da posicao
            if(color(positionCont)): #posicao tem cor
                if(len(groups) != 0): #existe grupos
                    groupsLast = groups[len(groups)-1] #ultima lista em groups
                    print "ULTIMA LISTA: " + str(groupsLast)

                    position = groupsLast[0]
                    positionLine = pos_l(position)
                    positionColumn = pos_c(position)
                    contentInGroupPosition = board[positionLine][positionColumn]

                    if(contentInGroupPosition == positionCont):
                    	groupsPos = make_pos(i,j)
                    	groupsLast.append(groupsPos)
                    else:
                    	groupsPos = make_pos(i,j)
                    	groups.append([groupsPos])
                    	print "FALSE"
                    print contentInGroupPosition
                else:
                    groupsPos = make_pos(i,j) #cria posicao correspondente ao conteudo
                    groups.append([groupsPos])
    print "GRUPOS:\n" + str(groups)

#board_remove_group(<board>, <group>) -> [5 valores]

# ------------------------------------ EXEMPLOS DE CHAMADAS ------------------------------------#
#draw_board([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])
#board_find_groups([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])
if(is_adjacent((1,2),(2,2))):
	print "TRUE"
else:
	print "FALSE"
