#just a scrpit to easily validate user input. 
#i wish i could use this part in my SPL project to make project more dynamic

def validateAnswer(answer):
  if answer.lower()=='yes':
    return True
  return False
  
print('Do you think 2+2=4?')
answer=input()
#removes any white space
answer=answer.strip()
if validateAnswer(answer):
  print('Your assumption is right!')
else:
  print('Noo, you guessed it wrong!')
  
