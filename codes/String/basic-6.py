# three types of formatting operations 

#first type
name = 'kitty'
luckyNumber = len(name)*3
print('hello {}, your lucky number is {}'.format(name,luckyNumber)) 

#second type
print('{luckyNumber}, is your lucky number {name}'.format(name='Shifa',luckyNumber=1301))

#third type
baseIncome = 1020
tax = .567
totalIncome =baseIncome*tax
print('base income = {}, tax = {}, totalIncome = {:.2f}'.format(baseIncome,tax,totalIncome))
