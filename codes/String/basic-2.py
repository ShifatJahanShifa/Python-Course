#initial message or string
message = 'A kong string it is, why?'
index = message.index('k')
print(index)
newMessage = message[:index] + 'l' + message[index+1:]
print(newMessage)

#index function
pets = 'Cats & Dogs'
print(pets.index('Dog'))
print(pets.index('s')) 

#using in keyword, returns true or false
print('Dragons' in pets)
print('Dogs' in pets)
