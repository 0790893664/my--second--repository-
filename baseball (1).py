class Get_score:
   def Event(self,user_event_input):
      if user_event_input=='homerun':
         return 'D'
      elif user_event_input=='catch':
         return 'C'
      elif user_event_input=='complete_score':
         return '5'
      else:
         return '-2'

   def calPoints(self, ops):

      stack = []
      mis=[]
      for i in ops:
          #int- the no of points we get in this point
          #sum of the last two valid round's points
         if i == "-2":
            mis.append(i)
            m=mis.count(i)
            if m==7:
               stack.clear()
               stack.append(-2)

            else:
               stack.append(0)
            #doubled score of the last valid round's points
         elif i == "D":
            stack.append(stack[-1] * 2)
            #the last valid round's points we get were invalid
         elif i == "C":
            stack.append(-2)
         else:
            stack.append(int(i))

      return sum(stack)
ob = Get_score()
user_input=[]
print("..........Enter Score as:\n\t\tHomerun\n \t\tCatch\n\t\tComplete_score\n\t\tMiss")
#print(ob.calPoints(['2', 'D','D','D']))
for i in range(1,8):
   print("............Round ",i,"...........")
   User_Event_Input=str(input("\tEnter Your Event:(Enter as string)\n")).lower()
   if User_Event_Input=='homerun' or User_Event_Input=='complete_score' or User_Event_Input=='miss' or User_Event_Input=='catch':
      event=Get_score().Event(User_Event_Input)
      user_input.append(event)
   else:
      print("You entered a Wrong Event")
      break

print("SCOREBOARD= ",user_input)
print("TOTAL SCORE=",ob.calPoints(user_input))
