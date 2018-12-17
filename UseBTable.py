# The BeautifulTable module has been installed and can be imported:

from beautifultable import BeautifulTable
# Create table by providing a name for the table and use BeautifulTable()
table = BeautifulTable()
# Create headers: table.column_headers = ['name1', 'name2', 'name3']
# Create rows: table.append_row(['x', 'x', 'x']) NOTE: both ([])
table.column_headers = ['name1', 'name2', 'name3']
table.append_row(['1', '2', '3'])
table.append_row(['4', '5', '6'])
table.append_row(['7', '8', '9'])
print(table)
