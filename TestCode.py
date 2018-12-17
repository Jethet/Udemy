#board is [' 1 |', ' 2 |', ' 3\n',  '4 |', ' 5 |', ' 6\n', '7 |', ' 8 |', ' 9\n']
"""
board = ['1 |', ' 2 |', ' 3\n',  '4 |', ' 5 |', ' 6\n',
        '7 |', ' 8 |', ' 9\n']
print(*board, sep='')
"""
"""
from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ['name', 'rank', 'gender']
table.append_row(['Jacob', '1', 'boy'])
print(table)
"""
from beautifultable import BeautifulTable
board = BeautifulTable()
board.append_row(['1', '2', '3'])
board.append_row(['4', '5', '6'])
board.append_row(['7', '8', '9'])
print(board)
