class stack:
  def __init__(self,size):
    self._a=[]
    self._top=None
    self._size=size
  def push(self,data):
    if self._top is not None:
      if self._top+1==self._size:
        print('stack overflow')
        return
    if self._top is None:
      ar=[0]
      self._top=0
      ar[self._top]=data
      self._a=ar
    else:
      ar=[0 for i in range(self._top+2)]
      #print(ar)
      for i in range(self._top+1):
        ar[i]=self._a[i]
      ar[-1]=data
      self._top+=1
      self._a=ar
    #print(self._a)
  #def apnd(self,ar.data):

  def peek(self):
    if self._top is None:
      return "we dont have any elemnts"
    return self._a[self._top]

  def pop(self):
    if self._top is None:
      print('stack underflow')
      return
    temp=self._a[-1]
    ar=[0 for i in range(self._top)]
    #print(ar)
    for i in range(self._top):
      ar[i]=self._a[i]
    self._top-=1
    if self._top < 0:
      self._top=None
    self._a=ar
    #print(self._a)
    return temp
stack=stack(3)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())