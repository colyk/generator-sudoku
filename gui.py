from tkinter import *
from tkinter import messagebox
from random import randint
from math import floor
  
root = Tk()
root.geometry('415x455+100+100')
root.title('SUDOKU by me)')
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

button1=Button(root,text='Проверить',width=15,height=2,font='arial 8')
button1.place(x ='20', y = '405')
entry = Entry(root,text = '25',width=15, font='arial 8')
entry.place(x ='150', y = '410')


button2=Button(root,text='Заново',width=15,height=2,font='arial 8')
button2.place(x ='300', y = '405')

m = 40 # размер ячеек
d = 3 # размер поля вокруг ячейки
nr = 9 # количество строк
nc = 9 # количество столбцов
x0 = m // 2 # отступ от левого края
y0 = m // 2 # отступ от вернего края

  
class cell():
    def __init__(self, r, c, n = ' ',color = '#fe8787'): # при создании указываем номер строки и столбца, в который помещаем
        self.n = n
        self.r = r # Номер сторки в двумерном списке.
        self.c = c # Номер столбца ...
        self.color = color
        if(n == ' ' and self.color == '#fe8787'):
            self.color = '#F0F0F8' 
        self.id = canv.create_rectangle(-100,0,-100,0,fill = self.color) # квадратик ячейки
        self.id_text = canv.create_text(-100,0, text = self.n, font = "Arial 18" )
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


def check_col(column = 0 ):
    tmp_table = [list(i) for i in zip(*table)]
    if (len(set(tmp_table[column])) == len(tmp_table[column])):
        return 0
    return 1


def check_row(row = 0):
    if(len(set(table[row])) == len(table[row])):
        return 0
    return 1


def check_block(k = 0, n = 0):
    k*=3
    n*=3
    set_ = set()

    for i in range(k,k+3):
        for j in range(n,n+3):
            set_.add(table[i][j])

    if(len(set_) == 9):
        return 0
    return 1

    
def check_solution(event):
    solution = 0
    for i in range(9):
        solution+=check_row(i)
        solution+=check_col(i)
    for i in range(3):
        for j in range(3):
            solution+=check_block(i,j)
    if(not solution):
        messagebox.showinfo( "Congratulate!" , 'sudoku is  solved!') 
    else:
        messagebox.showinfo( "Try again!" , 'sudoku is not solved!') 

def onEnter(event):
    pass
    # dificulty = int(entry.get())*24
    # if(dificulty<72):
    #     table = create_board()
    #     shufle()
    #     delete_elements()
    #     k()

def get_position(x, y):
    cc = floor(abs((d+x0-x+2)/m))
    rr = floor(abs((d+x0-y+2)/m))
    if(cc>5):
        cc = floor(abs((d+x0-x+8)/m))
    if(rr>5):
        rr = floor(abs((d+x0-y+8)/m))
    return (rr,cc)
 

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
    for i in range(mod):
        _change2 = randint(1,9)
        _change = randint(1,9)
        change(_change,_change2)
    transposing()


def delete_elements(dificulty = 15):
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

a = []
def write_table():
    rr = 0

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
            a[r].append(cell(r+rr,c+rc, table[r][c]) )

 

def click(event):
    x = event.x
    y = event.y
    aa,b = get_position(x, y)

    def key(event):
        try:
            dig = int(event.char)

        except Exception:
            messagebox.showinfo( "Congratulate!" , 'Не коректное значение') 
            return
        if(dig == 0):
            messagebox.showinfo( "Congratulate!" , 'Не коректное значение') 
            return
        table[aa][b] = dig
        new_top.destroy()
        write_table()
    if(table[aa][b] != ' '):
        return
    new_top = Toplevel()
    new_top.geometry('250x30+{}+{}'.format(100+x,100+y))
    w = Label(new_top, text="Введите значение с клавиатуры...")
    w.pack()
    new_top.bind('<Key>', key)
    new_top.focus_set()
    new_top.grab_set()


if __name__ == '__main__':
    table = create_board()
    shufle()
    delete_elements()
    write_table()
    
    canv.bind('<1>',click)
    button1.bind('<1>',check_solution)
    entry.bind("<Return>", onEnter)
    mainloop()