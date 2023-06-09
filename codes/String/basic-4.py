#count method
sentence = 'this is my country bangladesh, my homeland'
print(sentence.count('my'))

#endswith() method
name = 'Forest'
print('name (',name,') ends with "rest"=',name.endswith('rest'))

#isnumeric method
value = 'Forest'
print('value (',value,') is numeric=',value.isnumeric())
value = '12345'
print('value (',value,') is numeric=',value.isnumeric())

#short script before converting to int from string
value1 = '123'
value2 = '456'
value3 = 'Flower'

if value1.isnumeric() and value2.isnumeric():
  print(int(value1)+int(value2))
if value3.isnumeric() and value2.isnumeric():
  print(int(value3)+int(value2))
else:
  print('can\'t do it')
  
