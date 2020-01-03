import re

test_text = "This library app allows you to add a book, to search for an author or title,"
patterns = ('pa*', 'pa+', 'aa?', 'da?')
pattern2 = r'\s+'

for pattern in patterns:
    print(re.findall(pattern,test_text))

print(re.findall('[^,]+', test_text))
print(re.findall(pattern2, test_text))
