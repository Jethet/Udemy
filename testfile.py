import re

test_text = "This library app allows you to add a book, to search for an author or title,"
pattern = ['pa*', 'pa+']
print(re.search(pattern, test_text))
