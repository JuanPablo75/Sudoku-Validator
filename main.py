import collections
#Este programa coge una tabla bidimensional 9 * 9 y comprueba si es un sudoku resuelto correcatmente
# 1 - Comprueba numeros repetidos en filas
# 2 - Comprueba numeros repetidos en columnas
# 3 - Comprueba numeros repetidos en subCuadrados de 3 * 3

def valid_solution(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return False
            if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True