from random import randint

def create_board(n = 3):
    return [[ ((i*n + i//n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]


def print_board():
    spacer = "++---+---+---++---+---+---++---+---+---++"
    print(spacer)
    for i in range(9):
        print ("|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||".format(*table[i]))
        if((i+1)%3 == 0):
            print(spacer)


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


# def swap_row(k = 0, n = 1):
#     table[n],table[k] = table[k],table[n]


# def swap_col(k = 0, n = 1):
#     transposing()
#     swap_row(k,n)
#     transposing()


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


def delete_elements(dificulty = 20):
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
    
def solve():
    solution = 0
    for i in range(9):
        solution+=check_row(i)
        solution+=check_col(i)
    for i in range(3):
        for j in range(3):
            solution+=check_block(i,j)
    if(not solution):
        print('sudoku is solved!')
    else:
        print('Sudoku is nt solved!')

def main():
    shufle()
    # print_board()
    # solve()
    delete_elements()
    print_board()


if __name__ == '__main__':
    table = create_board()
    main()