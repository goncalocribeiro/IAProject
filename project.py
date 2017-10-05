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

#Auxiliar function to draw a board
#draw_board(<board>)
def draw_board(board):
    print(board)

#board_find_groups(<board>) -> [2 valores]

#board_remove_group(<board>, <group>) -> [5 valores]

draw_board([[1,2,3,4],[5,6,7,8]])
