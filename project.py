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
                if(len(groups) != 0):
                    groupsLast = groups[len(groups)-1] #ultima lista em groups
                    print "ULTIMA LISTA: " + str(groupsLast)

                    position = groupsLast[0]
                    position_line = pos_l(position)
                    position_column = pos_c(position)
                    contentInPosition = board[position_line][position_column]
                    print contentInPosition
                else:
                    groupsPos = make_pos(i,j) #cria posicao correspondente ao conteudo
                    groups.append([groupsPos])
    print groups

#board_remove_group(<board>, <group>) -> [5 valores]

# ------------------------------------ EXEMPLOS DE CHAMADAS ------------------------------------#
#draw_board([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])
board_find_groups([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]])
