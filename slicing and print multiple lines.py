
a = 'abcdef'
print('a = \'abcdef\'')
print('a[:3]',a[:3], 'a[::2]',a[::2], 'a[5:1:2]',a[5:1:2], sep = '\n')


print('a[1:5:2]',a[1:5:2], 'a[::-2]',a[::-2],\
      'a[5:1:-2]',a[5:1:-2], sep = '\n')


print('a[len(a):0:-1]',a[len(a):0:-1])

print('a.find("cd")',a.find('cd'))


b = 'hello world itcast and itcastcpp'
# 第29个字母不包含在搜索范围内
print('b.find("itcast", 14,29)',b.find("itcast", 14,29)) 



print('a.find("cd")',a.find('cd'))

print('a.index("cd")',a.index('cd'))

# 从右边开始找
print('a.rfind("cd")',a.rfind('cd'))


fName = 'dongGexxx.x.xx.py'

print('fName.rfind(".")',fName.rfind('.'))
index = fName.rfind('.')
print('fName[index:]',fName[index:])
print('fName.count(".")',fName.count('.'))

print("b.replace('it', 'IT')",b.replace('it', 'IT'))
print("b.replace('it', 'IT',1)",b.replace('it', 'IT',1))


print("b.split(' ')",b.split(' '))
