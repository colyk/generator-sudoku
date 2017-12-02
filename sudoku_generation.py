from random import randint

class Sudoku():
    def __init__(self, dificulty=20):
        self.dificulty = dificulty
        self.board = self.create_board()

    def create_board(self, n=3):
        return [[((i*n + i//n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]

    def print_board(self):
        spacer = "++---+---+---++---+---+---++---+---+---++"
        print(spacer)
        for i in range(9):
            print ("|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||".format(*self.board[i]))
            if (i + 1) % 3 == 0:
                print(spacer)

    def shufle_board(self, modification=10):
        for _ in range(modification):
            change_digit_1 = randint(1, 9)
            change_digit_2 = randint(1, 9)
            self.change(change_digit_2, change_digit_1)
        self.transposing()

    def change(self, change_digit_2, change_digit_1):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == change_digit_2:
                    self.board[i][j] = change_digit_1
                    continue
                if self.board[i][j] == change_digit_1:
                    self.board[i][j] = change_digit_2
                    continue

    def delete_elements(self):
        deleted_elements = []
        cell_count = randint(self.dificulty - 5, self.dificulty + 3)
        row_to_delete = randint(0,8)
        col_to_delete = randint(0,8)
    
        for i in range(cell_count):
            while (row_to_delete, col_to_delete) in deleted_elements:
                row_to_delete = randint(0,8)
                col_to_delete = randint(0,8)
            deleted_elements.append( (row_to_delete, col_to_delete) )
            self.board[row_to_delete][col_to_delete] = ' '

    def transposing(self):
        self.board = [list(i) for i in zip(*self.board)]

    def start_game(self):
        self.shufle_board()
        self.delete_elements()
        self.print_board()
    
    def check_columns(self, column):
        tmp_table = [list(i) for i in zip(*self.board)]
        if len(set(tmp_table[column])) == len(tmp_table[column]):
            return 0
        return 1
    
    def check_rows(self, row):
        if len(set(self.board[row])) == len(self.board[row]):
            return 0
        return 1
    
    def check_blocks(self, row, col):
        row *= 3
        col *= 3
        uniq_digits = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                uniq_digits.add(self.board[i][j])
        if(len(uniq_digits) == 9):
            return 0
        return 1

    def is_solved(self):
        not_soluted = 0
        for i in range(9):
            not_soluted += self.check_rows(i)
            not_soluted += self.check_columns(i)
        for i in range(3):
            for j in range(3):
                not_soluted += self.check_blocks(i, j)
        if not_soluted:
            return 0
        return 1
        

def main():
    game = Sudoku()
    print(game.is_solved())
    game.start_game()
    print(game.is_solved())


if __name__ == '__main__':
    main()
