import re
import urllib.request

f = urllib.request.urlopen(r'file:///D:\Install directory\python\ppt\breakfast.html')
text = f.read()
str = text.decode()
result = re.findall(r'<td>(\w+)</td>',str)
print(result)
for item in result:
    print('Item = %-15s' %(item))
f.close()