import os,sys,json,random
from datetime import *

#bad naming, no docstrings, mixed indent, unused imports, magic numbers, etc.
def main():
 a = input('name:')
 b = input('age:')
 try:
  b = int(b)
 except:
  b = 0
 c = {}
 c['n'] = a
 c['s'] = b*2.5+7
 c['t'] = datetime.now().strftime('%d-%m-%Y %H:%M')
 print('user:',a,'score:',c['s'])
 if b>18:
  print('adult')
 else:
  print('minor')
 if a=="admin":
  c['s']*=2
  print('admin bonus!')
 d = open('r.txt','w')
 d.write(str(c))
 d.close()
 for i in range(5):
  print('rand:',random.randint(1,100))

main()
