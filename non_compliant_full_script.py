X=100
Y=200
z=0
class test:
 def __init__(self,a):
  self.a=a
 def show(self):
  print('val:',self.a)
 def add(self,b):
  return self.a+b
 def sub(self,b):
  return self.a-b

def calc(x,y):
 global z
 z=x+y
 print('sum:',z)
 if x>y:
  print('x is big')
 else:
  print('y is big')

for i in range(0,3):
 calc(i,2)
 t=test(i)
 t.show()
 print('add:',t.add(5))
 print('sub:',t.sub(1))
print('X:',X)
print('Y:',Y)
print('z:',z)
