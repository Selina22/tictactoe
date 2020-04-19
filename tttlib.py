def genBoard():
   return [0,0,0,0,0,0,0,0,0]

def printBoard(T):
   if len(T) != 9:
      return False
   for i in T:
      if (i != 0) and (i != 1) and (i != 2):
         return False

   msg=[]
   pos=0
   for i in T:
      if (i==1):
         msg += ["X"]
      elif (i==2):
         msg += ["O"]
      else:
         msg += list(str(pos))
      pos+=1

   s = " " + msg[0] + " | " + msg[1] + " | " + msg[2]
   print(s)
   print("---|---|---")
   s = " " + msg[3] + " | " + msg[4] + " | " + msg[5]
   print(s)
   print("---|---|---")
   s = " " + msg[6] + " | " + msg[7] + " | " + msg[8]
   print(s)
   return True


def analyzeBoard(t):
   if t[0] == t[1] == t[2] != 0:
      return t[0]
   if t[3] == t[4] == t[5] != 0:
      return t[3]
   if t[6] == t[7] == t[8] != 0:
      return t[6]
   if t[0] == t[3] == t[6] != 0:
      return t[0]
   if t[1] == t[4] == t[7] != 0:
      return t[1]
   if t[2] == t[5] == t[8] != 0:
      return t[2]
   if t[0] == t[4] == t[8] != 0:
      return t[0]
   if t[2] == t[4] == t[6] != 0:
      return t[2]

   n_opens=0
   for i in t:
      if i==0:
         n_opens+=1
   if n_opens == 0:
      return 3
   else:
      return 0

import random

def genNonLoser(T,player):
   a=T[:]
   if player==2:
      opponent=1
   elif player==1:
      opponent=2
   else:
      return -1
   
   for j in range(0,9,1):
      if a[j]==0:
         a[j]=opponent
         state=analyzeBoard(a)
         if state==1 or state==2:
            return j
         a[j]=0
   return -1

def genWinningMove(T,player):
   a=T[:]
   if player==1:
      opponent=2
   elif player==2:
      opponent=1
   else:
      return -1
   
   for j in range(0,9,1):
      if a[j]==0:
        a[j]=player
        state=analyzeBoard(a)
        if state==1 or state==2:
            return j
        a[j]=0
   return -1

def genRandomMove(T,player):
   a=random.randint(0,8)
   if (player==1 or player==2) and T[a]==0:
     return a
   else:
     return -1

def genOpenMove(T,player):
   if T[4]==0:
     return 4
   elif T[0]==0:
     return 0
   elif T[2]==0:
     return 2
   elif T[6]==0:
     return 6
   elif T[8]==0:
     return 8
   elif T[1]==0:
     return 1
   elif T[3]==0:
     return 3
   elif T[5]==0:
     return 5
   elif T[7]==0:
     return 7
   else:
     return -1
