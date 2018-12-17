# The BeautifulTable module has been installed and can be imported:
from beautifultable import BeautifulTable
#Create table by providing a name for the table and use BeautifulTable()
table = BeautifulTable()
#Create headers: table.column_headers = ['name1', 'name2', 'name3']
#Create rows: table.append_row(['x', 'x', 'x']) NOTE: both ([])
table.column_headers = ['name1', 'name2', 'name3']
table.append_row(['1', '2', '3'])
table.append_row(['4', '5', '6'])
table.append_row(['7', '8', '9'])
print(table)
#Create new column: table.append_column('NAME'), ['DATA', 'D', 'D', 'D'])
#Watch out for the use of both () and []
table.append_column('player', ['X', 'O', 'X'])
print(table)

#You can also build a new table using slicing: the new table retains
#the properties of the original, it is a copy of the data.
new_table = table[:3]
print(new_table)
#HEADER DOES NOT COUNT AS A ROW ???
#You can access a row using its index:
print(list(table[1]))
#You can access a field of a row via A) the index or B) the header
#A)
print(table[2][3])
#B)
print(table[1]['player'])
#You can access a column using header names (watch out for DUPLICATE
#HEADERS) or using index. The column returned is an iterator, not a list.
print(list(table['name3']))
print(list(table))
