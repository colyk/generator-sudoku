from tkinter import *
from random import *
  
root = Tk()
root.geometry('415x415')
root.title('SUDOKU')
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
 
 
m = 40 # размер ячеек
d = 3 # размер поля вокруг ячейки
nr = 9 # количество строк
nc = 9 # количество столбцов
x0 = m // 2 # отступ от левого края
y0 = m // 2 # отступ от вернего края

  
class cell():
    def __init__(self, r, c, n = ' '): # при создании указываем номер строки и столбца, в который помещаем
        self.n = n
        self.r = r # Номер сторки в двумерном списке.
        self.c = c # Номер столбца ...
        self.color = 'white' #choice(colors) # случайный цвет из списка
        self.id = canv.create_rectangle(-100,0,-100,0,fill = self.color) # квадратик ячейки
        self.id_text = canv.create_text(-100,0, text = self.n, font = "Arial 18" )
        if(r!= -1 and c!=-1):
            self.paint()
  
    def paint(self):
        x1 = x0 + self.c * m + d
        # рассчитать координаты левого верхнего угла.
        y1 = y0 + self.r * m + d
        # координаты правого нижнего угла.
        x2 = x1 + m - 2*d  #- r
        y2 = y1 + m - 2*d
        canv.coords(self.id,x1,y1,x2,y2)
        canv.itemconfig(self.id,fill = self.color)
        # текст в центр ячейки
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        canv.coords(self.id_text,x,y)
        canv.itemconfig(self.id_text, text = self.n)
  
c_test = cell(-1,-1)
 
def change(k,n):
    for i in range(9):
        for j in range(9):
            if(table[i][j] == k):
                table[i][j] = n
                continue
            if(table[i][j] == n):
                table[i][j] = k
                continue


def transposing():
    global table
    table =  [list(i) for i in zip(*table)]

def create_board(n = 3):
    return [[ ((i*n + i//n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]

def shufle(mod = 10):
    # a = []
    # _change,_change2 = 1,2
    #     while((_change*100+_change2*10) in a and _change2 != _change):
        # a.append(_change*100+_change2*10)
        # print(_change,_change2)
    for i in range(mod):
        _change2 = randint(1,9)
        _change = randint(1,9)
        change(_change,_change2)

    transposing()

def delete_elements(dificulty = 35):
    cell_count = randint(dificulty - 5, dificulty+3)
    a = []
    row_to_delete = randint(0,8)
    col_to_delete = randint(0,8)

    for i in range(cell_count):
        while( (row_to_delete,col_to_delete) in a):
            row_to_delete = randint(0,8)
            col_to_delete = randint(0,8)
        a.append( (row_to_delete,col_to_delete) )
        table[row_to_delete][col_to_delete] = ' '

table = create_board()
shufle()

delete_elements()
# for i in range(9):
#     for j in range(9):
#         print(table[i][j])

rr = 0
a = []
for r in range(nr): 
    aa = 0
    a.append([]) 
    rc = 0
    for c in range(nc): 

        if(r%3 == 0 and r!=0 and aa<1):
            rr+=0.2
            rr = round(rr,1)
            aa+=1
        if(c%3 == 0 and c!=0 ):
            rc+=0.2
            rc = round(rc,1)
        a[r].append(cell(r+rr,c+rc, table[r][c]) )# добавляем очередной элемент в строку
 
mainloop()
